def string_reverse(string):
    """Return the string argument in reverse."""
    reversed_string = ""
    temp = list(string)

    for i in range(len(temp)):
        reversed_string += temp[len(temp)-1-i]
    
    return reversed_string

str1 = "Test String"
str2 = "Bruno Grego"

print(string_reverse(str1))
print(string_reverse(str2))

print(str1[::-1])
print(str2[::-1])