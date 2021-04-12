import sys
sys.setrecursionlimit(10000000000000)
if __name__ == "__main__":
    C = int(input())
    SWITCHES = 10
    CLOCKS = 16

    connectedClocks = [[0, 1, 2], [3, 7, 9, 11], [4, 10, 14, 15], [0, 4, 5, 6, 7], [6, 7, 8, 10, 12],
                       [0, 2, 14, 15], [3, 14, 15], [4, 5, 7, 14, 15], [1, 2, 3, 4, 5], [3, 4, 5, 9, 13]]
    # 스위치를 누르는 순서는 중요하지 않다.
    # 각 스위치를 해당하는 숫자 만큼만 누르면 완성된다.
    # 각 스위치를 몇번씩 누르면 완성되는지 구해야함.
    def checkAligned(iClock):
        ret = True

        for i in range(CLOCKS):
            if iClock[i] != 12:
                ret = False
                break

        return ret

    def push(iClock, switch):
        for clock in connectedClocks[switch]:
            iClock[clock] += 3
            if iClock[clock] == 15:
                iClock[clock] = 3

    def recursiveSolve(iClock, switch):
        if switch == SWITCHES:
            if checkAligned(iClock):
                return 0 # 정렬됨
            else:
                return float('inf') # 정렬안됨
        ret = float('inf')

        for i in range(4):
            ret = min(ret, i + recursiveSolve(iClock, switch+1))
            push(iClock, switch)

        return ret
    while C:
        C -= 1
        clocks = list(map(int, input().split()))
        answer = recursiveSolve(clocks, 0)
        if answer == float('inf'):
            print(-1)
        else:
            print(answer)