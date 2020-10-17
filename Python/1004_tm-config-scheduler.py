''' ---------------------------------------------------------------------------------------------------------------- '''
''' Imports '''

import os
import time
import subprocess

''' ---------------------------------------------------------------------------------------------------------------- '''
''' Macros '''

# Paths
home_path = "/home/ctw00982"
testsuite_path = home_path + "/testmanager/src/ascgit156.tmgr-personalization/testsuites"
scheduler_path = home_path + "/testmanager/scheduler/run.d"

excluded_tests = ["hardware_deploy_debug_token_deletes_persistence",
                  "hardware_e2e_create_cd_accounts",
                  "hardware_e2e_sync_from_backend",
                  "hardware_e2e_user_account_proxy_available",
                  "hardware_genius_mode_activate_profile",
                  "hardware_instant_on",
                  "hardware_instant_on_connected_drive",
                  "hardware_pem_instant_on",
                  "hardware_smart_access_version"]

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

# Print excluded tests
print("Excluded tests:")

for i in range(len(excluded_tests)):
    print(excluded_tests[i])

print()

# ls -l <scheduler_path>
scheduler_content = get_ls_output(scheduler_path)

# Remove test files from <scheduler_path>
print("Remove test files from <scheduler_path>:")

for i in range(len(scheduler_content)):
    words = scheduler_content[i].split()
    file_name = words[-1]

    if (file_name != "README"):
        cmd = "rm " + scheduler_path + "/" + file_name
        print(cmd)
        os.system(cmd)

print()

time.sleep(1)

# ls -l <testsuite_path>
testsuite_content = get_ls_output(testsuite_path)

# Create new test files in <scheduler_path>
print("Create new test files in <scheduler_path>:")

for i in range(len(testsuite_content)):
    words = testsuite_content[i].split()
    test_name = words[-1]

    if (excluded_tests.count(test_name) == 0):
        if (i < 10):
            prefix = "00"
        elif (i < 100):
            prefix = "0"
        
        file_name = prefix + str(i) + "_" + test_name
        
        cmd = "touch " + scheduler_path + "/" + file_name
        print(cmd)
        os.system(cmd)

print()
