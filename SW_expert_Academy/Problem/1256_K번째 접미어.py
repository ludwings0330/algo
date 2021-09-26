TC = int(input())
for testCase in range(1, TC+1):
    K = int(input())
    userInputString = input()
    userInputStringList = []

    for i in range(len(userInputString)):
        userInputStringList.append(userInputString[i:])
    userInputStringList.sort()
    K -= 1
    ans = ''
    if K >= len(userInputStringList):
        ans = None
    else:
        ans = userInputStringList[K]

    print("#{} {}".format(testCase, ans))