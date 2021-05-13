def recursiveSolve(strTmpList, k):
    global count
    if k == 0:
        count += 1

        if count == n :
            return ''.join(strTmpList)
        else:
            return ''

    ret = ''

    for i in range(len(strList)):
            if not visit[i] and ret =='':
                visit[i] = True
                strTmpList.append(strList[i])

                ret = recursiveSolve(strTmpList, k-1)
                # 한 종류의 최적값 이라고 할 수 있지.
                strTmpList.pop()
                visit[i] = False
    return ret

while True:
    try:
        count = 0
        strList, n = input().split()
        strList = list(strList)
        n = int(n)

        visit = [False]*len(strList)

        answer = recursiveSolve([], len(strList))

        print(''.join(strList) , str(n) , '=', sep=' ', end=' ')
        if answer =='':
            print('No permutation')
        else:
            print(answer)


    except:
        break