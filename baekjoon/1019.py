# Title ; 책 페이지
# Tag ; 수학

origin_N = list(map(int, list(input().rstrip())))
N = origin_N[:]

digits = [0] * 10
k = len(N) - 1
# 10의 k 승
# 0~N 몇번 나오는지 세고, 0 한개 줄이기

idx = 0
while idx <= k:
    for i in range(idx):
        # N[idx] == 0 일때, 처리
        tmp = N[idx] * (10**(k-idx))
        digits[origin_N[i]] += tmp

    digits[N[idx]] += 1
    N[idx] -= 1

    while N[idx] >= 0:
        digits[N[idx]] += 10**(k - idx)
        N[idx] -= 1
    if k != idx:
        for i in range(10):
            digits[i] += ((k - idx) * (10**(k-idx-1)))*origin_N[idx]
        if idx == 0:
            for i in range(k+1):
                digits[0] -= 10**i
    idx += 1
if k == 0:
    digits[0] -= 1
print(*digits)