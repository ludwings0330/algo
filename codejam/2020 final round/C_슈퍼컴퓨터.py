import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())
while TC:
    TC -= 1
    N = int(input())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    programs = list(zip(H, D, [i for i in range(N+1)]))
    programs.sort(key=lambda x:x[1])

    C = [0] * N
    C[0] = programs[0][0]
    for i in range(1, N):
        C[i] = C[i-1] + programs[i][0]
        # i 번째 프로그램이 끝나는 시간

    for i in range(0, N):
        C[i] = max(0, C[i] - programs[i][1])
        # 각 프로그램별 지각도 저장

    for i in range(1, N):
        C[i] = max(C[i], C[i-1])
        # i 번째에서의 최대 지각도

    # 최우선처리대상 처리를 통해
    # 최대 지각도의 최소값 구하기
    ans = max(0, C[-1] + 1 - programs[0][0])
    for i in range(1, N):
        diff = 1 - programs[i][0]

        # 최우선 처리 대상을 처리했을때의 최대지각도
        compare = max(0, C[i-1], C[-1] + diff)

        # 최대지각도의 최소값 처리
        ans = min(ans, compare)

    print(ans)