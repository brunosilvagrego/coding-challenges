if __name__ == '__main__':
    N = int(input())

    CMD_INSERT = "insert"
    CMD_PRINT = "print"
    CMD_REMOVE = "remove"
    CMD_APPEND = "append"
    CMD_SORT = "sort"
    CMD_POP = "pop"
    CMD_REVERSE = "reverse"

    arr = []

    for i in range(N):
        cmd = str(input())

        args = cmd.split(" ")

        if (len(args) == 3 and (args[0] == CMD_INSERT)):
            # insert
            i = int(args[1])
            e = int(args[2])
            arr.insert(i, e)

        elif (len(args) == 2):
            # remove
            if (args[0] == CMD_REMOVE):
                args = cmd.split(" ")
                e = int(args[1])
                arr.remove(e)

            # append
            elif (args[0] == CMD_APPEND):
                args = cmd.split(" ")
                e = int(args[1])
                arr.append(e)

        elif (len(args) == 1):
            # print
            if (args[0] == CMD_PRINT):
                print(arr)
            
            # sort
            elif (args[0] == CMD_SORT):
                arr.sort()

            # pop
            elif (args[0] == CMD_POP):
                arr.pop()

            # reverse
            elif (args[0] == CMD_REVERSE):
                arr.reverse()
