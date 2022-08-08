import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

# s index 에 값을 채울 것이다.
# s index에 들어가는 값은 움직일 수 있는 범위내에서 가장 큰 값
# 움직일 수 있는 범위는 s~s+S 또는 s~N-1
for s in range(N):
    MAX_idx = 0
    MAX = 0
    for i in range(s, min(s+S+1, N)):
        if MAX < arr[i]:
            MAX = arr[i]
            MAX_idx = i

    # MAX_idx 를 s로 옮겨온다
    for k in range(MAX_idx, s, -1):
        if arr[k] > arr[k-1]:
            arr[k], arr[k-1] = arr[k-1], arr[k]
            S -= 1
    if S == 0:
        break
print(*arr)
