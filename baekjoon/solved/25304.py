X = int(input())
N = int(input())
total = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    total += arr[0] * arr[1]
print('Yes' if total == X else 'No')