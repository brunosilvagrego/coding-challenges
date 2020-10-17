''' ---------------------------------------------------------------------------------------------------------------- '''
''' Imports '''

import os
import sys
import subprocess
import xml.etree.ElementTree as XML

''' ---------------------------------------------------------------------------------------------------------------- '''
''' Macros '''

# Paths
home_path = "/home/ctw00982"
tm_results_path = home_path + "/testmanager/results"
results_file = "testmanager_results.xml"

''' ---------------------------------------------------------------------------------------------------------------- '''
''' Classes '''

class color:
    """ Class to store text colors Macros """
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class TestResult(object):
    """ Class to store test result parameters """
    def __init__(self, test_name, run_result, execution_time, timestamp):
        self.test_name = test_name
        self.run_result = run_result
        self.execution_time = execution_time
        self.timestamp = timestamp

''' ---------------------------------------------------------------------------------------------------------------- '''
''' Functions '''

def get_ls_output(dir_path):
    """ Get ls command output for a given directory path.
    Args:
        dir_path (str): Given directory path.
    Returns:
        ls_strings (list): List containing ls output in str format.
    """

    # ls -l <dir_path>
    out = subprocess.Popen(["ls", "-l", dir_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()

    # Decode ls command output
    ls_output = stdout.decode('utf-8')
    ls_strings = ls_output.split("\n")

    # Remove last line (empty string)
    ls_strings.pop()

    # Remove first line (total <N>)
    ls_strings.reverse()
    ls_strings.pop()
    ls_strings.reverse()

    # Return strings list
    return ls_strings

''' ---------------------------------------------------------------------------------------------------------------- '''
''' Main '''

error = False

# Too few arguments
if (len(sys.argv) < 4):
    print("ERROR: Too few arguments")
    error = True

# Too many arguments
elif (len(sys.argv) > 4):
    print("ERROR: Too many arguments")
    error = True

if (error):
    print("cmd: python3 <path_to_script>/tm-check-results.py <MGU_Version> <SINT_JOB> <target_type>")
    print("e.g: python3 <path_to_script>/tm-check-results.py 20w41.5-1_MGU SINT_JOB_3414 vmwx86_21")
    sys.exit()

# ls -l <results_path>
results_path = tm_results_path + "/" + sys.argv[1] + "/" + sys.argv[2] + "/" + sys.argv[3]

# Get ls -l <results_path> output
results_content = get_ls_output(results_path)

# Testsuite results list
testsuite_results = []

# Longest name length
longest_name_length = 0

# Parse testmanager_results.xml
for i in range(len(results_content)):
    # Get the words of each line of ls -l <results_path> output
    words = results_content[i].split()

    # Get the test results directory name
    test_dir = words[-1]
    test_dir_strings = test_dir.split("__")

    # Get test name
    test_name = test_dir_strings[0]

    # Get test timestamp
    temp = test_dir_strings[1]
    timestamp = temp[0:4] + "/" + temp[4:6] + "/" + temp[6:8] + ", " + temp[9:11] + ":" + temp[11:13] + ":" + temp[13:]

    # Create results file path
    results_file_path = results_path + "/" + test_dir + "/" + results_file

    # Pass the path of the XML document to enable the parsing process
    xml_doc = XML.parse(results_file_path)

    # Get the parent tag of the XML document
    root = xml_doc.getroot() 
        
    # Get test results attributes
    errors = root.get("errors")
    failures = root.get("failures")
    execution_time = root.get("time")
    
    # Determine run result
    if ((errors != "0") or (failures != "0")):
        run_result = "FAIL"
    else:
        run_result = "PASS"
    
    # Store test results in a TestResult object
    test_result = TestResult(test_name, run_result, float(execution_time), timestamp)

    # Append test result to testsuite results list
    testsuite_results.append(test_result)

    # Determine longest name
    name_length = len(test_name)

    if (name_length > longest_name_length):
        longest_name_length = name_length

# To format output
longest_name_length += 3    

# Testsuite statistics
testsuite_pass_count = 0
testsuite_fail_count = 0
testsuite_execution_time = 0.0

# Print testsuite results
print("Testsuite Results:")

for i in range(len(testsuite_results)):
    # Print test name
    print(testsuite_results[i].test_name, end ="")
    print(":  ", end ="")

    # Print filling
    filling = longest_name_length - len(testsuite_results[i].test_name)
    print("-" * filling, end ="")

    # Determine text color and count PASS/FAIL occurrences
    text_color = ""

    if (testsuite_results[i].run_result == "FAIL"):
        text_color = color.RED + color.BOLD
        testsuite_fail_count += 1
    elif (testsuite_results[i].run_result == "PASS"):
        text_color = color.GREEN + color.BOLD
        testsuite_pass_count += 1

    # Print test run result
    print(text_color + "  " + testsuite_results[i].run_result + color.END, end="  |  ")

    # Print test execution time
    blank_space = ""

    if (testsuite_results[i].execution_time < 100.0):
        blank_space = " "

    print(color.BOLD + blank_space + "{:.1f}".format(testsuite_results[i].execution_time) + " s" + color.END, end="  |  ")

    # Print test timestamp
    print(color.BOLD + testsuite_results[i].timestamp + color.END)

    # Update testsuite execution time
    testsuite_execution_time += testsuite_results[i].execution_time


# Calculate testsuite total executed tests
testsuite_total_tests = len(testsuite_results)

# Calculate PASS/FAIL percentages
pass_percentage = testsuite_pass_count / testsuite_total_tests * 100
fail_percentage = testsuite_fail_count / testsuite_total_tests * 100

# Outputs
total_str = "Total: " + str(testsuite_total_tests)
total_percentage = "100.0 %"
pass_str = "PASS: " + str(testsuite_pass_count)
pass_percentage_str = "{:.1f} %".format(pass_percentage)
fail_str = "FAIL: " + str(testsuite_fail_count)
fail_percentage_str = "{:.1f} %".format(fail_percentage)

# Calculate blank spaces
blank_spaces = [0, 0, 0, 0]
blank_spaces[0] = len(total_str) - len(pass_str)
blank_spaces[1] = len(total_percentage) - len(pass_percentage_str)
blank_spaces[2] = len(total_str) - len(fail_str)
blank_spaces[3] = len(total_percentage) - len(fail_percentage_str)

# Print testsuite statistics
# Total
print("\nTestsuite Statistics:")
print(total_str, end="  |  ")
print(total_percentage)

# PASS
print(color.GREEN + color.BOLD + "PASS" + color.END, end=": ")
print(" " * blank_spaces[0], end ="")
print(testsuite_pass_count, end="  |  ")
print(" " * blank_spaces[1], end ="")
print(pass_percentage_str)

# FAIL
print(color.RED + color.BOLD + "FAIL" + color.END, end=": ")
print(" " * blank_spaces[2], end ="")
print(testsuite_fail_count, end="  |  ")
print(" " * blank_spaces[3], end ="")
print(fail_percentage_str)

# Total Execution Time
print("\nTotal Execution Time:  " + "{:.1f} s".format(testsuite_execution_time) + "  |  "
                                  + "{:.1f} min".format(testsuite_execution_time/60) + "  |  "
                                  + "{:.1f} hours\n".format(testsuite_execution_time/3600) )
