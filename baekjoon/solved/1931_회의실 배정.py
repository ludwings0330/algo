import sys

if __name__ == "__main__":
    N = int(input())
    meetingTime = []
    # 0 <= meetingTime <= 2^31 -1
    for i in range(N):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        meetingTime.append([start, end])

    meetingTime = sorted(meetingTime, key = lambda x:(x[1], x[0]))

    nStart = meetingTime[0][0]
    nEnd = meetingTime[0][1]
    count = 1

    for start, end in meetingTime[1:]:
        if nEnd > start :
            continue
        else:
            nStart = start
            nEnd = end
            count += 1

    print(count)
