def count_substring(string, sub_string):
    count = 0
    pos = 0
    remaining_chars = len(string)
    sub_string_length = len(sub_string)

    while (remaining_chars >= sub_string_length):
        pos = string.find(sub_string, pos)

        if (pos == -1):
            remaining_chars = 0
        else:
            pos += 1
            count += 1
            remaining_chars -= pos

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)