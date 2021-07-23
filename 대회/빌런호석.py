import sys
input = sys.stdin.readline

N, K, P, X = map(int, input().rstrip().split())

# 1 ~ N 층
# 최대 K자리의 수가 표시된다
# 1 ~ P 개를 반전 시킨다
# 엘리베이터는 현재 X 층이다
# 반전시킬 LED를 고를 수 있는 경우의 수

nums = {0:0b1110111, 1:0b0010010, 2:0b1011101, 3: 0b1011011, 4:0b0111010, 5:0b1101011, 6:0b1101111,
        7:0b1010010, 8:0b1111111, 9:0b1111011}
def count(n):
    ret = 0
    while n:
        if n & 1:
           ret += 1
        n = n >> 1
    return ret

ans = 0
for l in range(1, N+1): # 1층부터 N층
    cnt = 0
    tX = X
    tl = l

    for _ in range(K):
        n = tX%10
        tX //= 10

        j = tl%10
        tl //= 10

        t = nums[n]^nums[j]
        cnt += count(t)

        if cnt > P:
            break

    if 1 <= cnt <= P:
        ans+=1

print(ans)