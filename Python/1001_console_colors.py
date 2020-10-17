class color:
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

print("Test 01: ", end =" ") 
print(color.GREEN + color.BOLD + 'PASS' + color.END)

print("Test 02: ", end =" ")
print(color.RED + color.BOLD + 'FAIL' + color.END)

print("Test 03: ", end =" ")
print(color.BLUE + color.BOLD + color.UNDERLINE + 'EXCLUDED' + color.END)
