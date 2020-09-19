# Inputs:
# 4
# Prashant
# 32
# Pallavi
# 36
# Dheeraj
# 39
# Shivam
# 40

if __name__ == '__main__':
    l = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([score, name])

    l.sort()

    minScore = l[0][0]
    runnerDown = l[0][0]

    search = True
    i = 0
    n = len(l)
    names = []

    while (i < n):
        if ((l[i][0] == runnerDown) and (search == False)):
            names.append(l[i][1])

        if ((l[i][0] > runnerDown) and (search == True)):
            runnerDown = l[i][0]
            names.append(l[i][1])
            search = False

        i = i + 1

    names.sort()

    for name in names:
        print(name)
