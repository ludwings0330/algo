import sys
sys.setrecursionlimit(100000000)
switch = [[0, 1, 2],
          [3, 7, 9, 11],
          [4, 10, 14, 15],
          [0, 4, 5, 6, 7],
          [6, 7, 8, 10, 12],
          [0, 2, 14, 15],
          [3, 14, 15],
          [4, 5, 7, 14, 15],
          [1, 2, 3, 4, 5],
          [3, 4, 5, 9, 13]]

C = int(input())
def pushSwitch(sw, n):
    # sw : 스위치 번호 n : 누른 횟수
    for i in switch[sw]:
        clocks[i] += 3
        if clocks[i] == 15:
            clocks[i] = 3

def recursiveSolve(sw):
    finished = True
    if sw >= 10:
        # sw 는 0~ 9

        for i in range(len(clocks)):
            if clocks[i] != 12:
                finished = False
                break

        if finished:
            return 0
        else:
            return float('inf')


    ret = float('inf')

    for i in range(4): # 최대 3번 까지 누름
        ret = min(i + recursiveSolve(sw+1), ret)
        pushSwitch(sw, 1)

    return ret

while C:
    C -= 1
    clocks = list(map(int, input().split()))
    answer = recursiveSolve(0)
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)