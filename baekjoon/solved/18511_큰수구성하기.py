N, numOfK = map(int, input().split())
K = list(map(int, input().split()))

def recursiveSolve(compNum):
    if compNum > N:
        return 0
    else:
        ret = compNum

        for i in range(numOfK):
            ret = max(ret, recursiveSolve(compNum*10 + K[i]))

    return ret


print(recursiveSolve(0))
