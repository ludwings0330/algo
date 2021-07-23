import sys
input = sys.stdin.readline

# n개의 시계
# i번째 시계가 가리키고 있는 시각 T[i]
# 매초 D[i]초 만큼 시간이 증가한다

# 모두 시간이 같으면 "동기화" 24시간 동안 n 개의 시계가 몇번 동기화 될까?
# 86400
T = int(input())

while T:
    T -= 1
    n = int(input())
    tclocks = input().rstrip().split()
    clocks = []
    D = list(map(int, input().rstrip().split()))
    times = []
    ans = 0
    times_dict = {}

    for i in range(n):
        D[i] %= 86400

    for i in range(n):
        clocks.append(list(map(int, tclocks[i].split(':'))))
        times.append(60*60*clocks[i][0] + 60*clocks[i][1] + clocks[i][2])

    for t in range(86400):
        nextTime = times[0] + t*D[0]
        if nextTime >= 86400:
            nextTime %= 86400
        times_dict[t] = nextTime

    for i in range(1, n):
        ntimes_dict = {}
        cnt = 1
        for t, time in times_dict.items():
            nextTime = times[i] + t*D[i]
            if nextTime >= 86400:
                nextTime %= 86400
            if time == nextTime:
                ntimes_dict[t] = time
                cnt -= 1
                if cnt < 0:
                    break
                continue
            cnt = 1
        else:
            times_dict = ntimes_dict
    print(len(times_dict))