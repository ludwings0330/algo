import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

while TC:
    TC -= 1
    N = int(input())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    programs = list(zip(H, D, [i for i in range(N)]))
    programs.sort(key = lambda x:x[1]) # 데드라인 순으로 정렬

    C = [0] * N
    C[0] = programs[0][0]
    delay = []
    for i in range(1, N):
        C[i] = C[i-1] + programs[i][0]
        delay.append(max(0, C[i] - programs[i][1]))


    print(programs)