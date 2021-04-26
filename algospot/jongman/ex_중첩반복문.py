def recursivePrint(n, picked, nowList):
    if picked == 4:
        print(nowList)
        return
    if picked == 0:
        k = 0
    else:
        k = nowList[-1]

    for i in range(k+1, n+1):
        nowList.append(i)
        recursivePrint(n, picked+1, nowList)
        nowList.pop()

    pass

if __name__ == "__main__":
    n = int(input())
    recursivePrint(n, 0, [])

    pass
