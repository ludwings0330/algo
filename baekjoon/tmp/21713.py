N, K = map(int, input().split())
# 3 < N <= 20 , 0 <= K < N-2
arr = list(map(float, input().split()))
A = float(input())

arr.sort()

# K 개를 제거하고 평균을 낸다.
# 그런데 이놈이 K개 중에 최대하고 최소값을 제거했다.
# 어떤 값들이 제거 되어있는지 출력
# N - K - 2 개 선택해서 평균이 A 면 출력

# ans_idx에는 추가한 값들이 있음
def solve(remains, idx, total, ans_idx):
    if remains == 0:
        total.sort()
        if round(sum(total[1:-1]) / (N-K-2), 2) == A:
            print("%.2f %.2f" %(total[0], total[-1]), end=' ')
            return set(ans_idx)
        else:
            return []

    for next in range(idx+1, N):
        ret = solve(remains - 1, next, total + [arr[next]], ans_idx + [next])
        if ret:
            return ret
    return []

k = solve(N - K, -1, [], [])

for i in range(N):
    if i in k:
        continue
    else:
        print("%.2f" %(arr[i]), end=' ')
