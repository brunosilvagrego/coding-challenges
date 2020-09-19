# Inputs:
# 5
# 2 3 6 6 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    l = list(arr)
    l.sort()
    
    maxScore = l[n-1]
    runnerUp = l[n-1]

    search = True
    i = n-2

    while ((i >= 0) and (search == True)):
        if (l[i] < runnerUp):
            runnerUp = l[i]
            search = False

        i = i - 1

    print(runnerUp)


