str_result = "PIA ID: {0:#0{1}x}, ".format(1091, 5) + \
             "PIA Value {0:#0{1}x}".format(1073741825, 10)

print(str_result)


stdout = '''Enabled
All operations successful.
'''

print(stdout)
print(str(stdout).split("\n")[0])