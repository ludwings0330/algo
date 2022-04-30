
# 최대공약수
def gcd(n, m):
    # gcd(n, m) = gcd(m, r)
    # r 은 n을 m으로 나눈 나머지
    if n < m:
        n, m = m, n
    if m == 0:
        return n
    return gcd(m, n % m)

# 최소공배수
def lcm(n, m):
    return (n * m) // gcd(n, m)
    return 0


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

print(gcd(12, 128))
solution(3, 12)
solution(2, 5)
