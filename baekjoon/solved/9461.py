#파도반 수열
arr = [0] + [1, 1, 1] + [0]*101
for i in range(4, 101):
    arr[i] = arr[i-3] + arr[i-2]
T = int(input())
for _ in range(T):
    N = int(input())
    print(arr[N])