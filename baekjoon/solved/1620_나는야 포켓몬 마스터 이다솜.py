import sys

if __name__ == "__main__":
    N, M = map(int, input().split())
    pocketmons = {}
    num =1
    for i in range(N):
        pocketmons[sys.stdin.readline().rstrip()] = num
        num+=1

    listOfName = list(pocketmons.keys())
    listOfNum = list(pocketmons.values())
    for i in range(M):
        Q = sys.stdin.readline().rstrip()
        if Q in pocketmons:
            print(pocketmons[Q])
        else:
            Q = int(Q)
            print(listOfName[Q-1])