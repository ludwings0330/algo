import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(input())

red_cnt = 0
blue_cnt = 0

if len(arr) == 1:
    print(0)
else:
    i = len(arr)-1
    while i > 0 and arr[i] == arr[i-1]:
        i -= 1
    for j in range(i):
        if arr[j] == 'R':
            red_cnt += 1
        else:
            blue_cnt += 1
    ans = min(red_cnt, blue_cnt)
    red_cnt = 0
    blue_cnt = 0
    i = 0
    while i < N-1 and arr[i] == arr[i+1]:
        i += 1
    for j in range(i+1, N):
        if arr[j] == 'R':
            red_cnt += 1
        else:
            blue_cnt += 1

    ans = min(ans, red_cnt, blue_cnt)

    print(ans)
