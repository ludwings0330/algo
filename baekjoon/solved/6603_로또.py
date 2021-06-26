def printLotto(stackList):
    print(' '.join(str(_) for _ in stackList))

def Lotto(index, stackList):
    if index == k+1:
        return
    elif len(stackList) == 6:
        printLotto(stackList)
    else:
        for i in range(index, k):
            stackList.append(S[i])
            Lotto(i+1, stackList)
            stackList.pop()


while True:
    inputList = list(map(int, input().split()))
    if len(inputList) == 1:
        break

    k = inputList[0]
    S = inputList[1:]

    Lotto(0, [])
    print()

