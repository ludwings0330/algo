N, K = map(int, input().split())
kit = list(map(int, input().split()))
use = [False] * N

def recursiveSolve(kg, day, use):
    if kg < 500:
        return 0
    if day == N:
        return 1

    ret = 0

    for i in range(len(kit)):
        if not use[i]:
            use[i] = True
            ret +=  recursiveSolve(kg-K+kit[i], day + 1, use)
            use[i] = False

    return ret


answer = recursiveSolve(500, 0, use)
print(answer)