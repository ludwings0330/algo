import sys
input = sys.stdin.readline

T = int(input().rstrip())
while T:
    T -= 1
    n = int(input().rstrip())
    choice = [0]
    l = list(map(int, input().split()))
    choice += l
    ret = []
    visit = [False] * (n+1)
    for i in range(1, n+1):
        if not visit[i]:
            next = i
            while True:
                if visit[next]:
                    break
                else:
                    visit[next] = True
                    next = choice[next]
            if next != i:
                tmpnext = i
                while True:
                    ret.append(tmpnext)
                    tmpnext = choice[tmpnext]
                    if tmpnext == next:
                        break
    # print(ret)
    print(len(ret))