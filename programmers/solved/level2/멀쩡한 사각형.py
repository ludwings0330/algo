# 가로 W, 세로 H 직사각
# 격자 형태 1 cm
# 대각선이 그어져 있는 상태, 사용할 수 있는 정사각형의 개수를 구하는 solution


def gcd(n, m):
    if n < m:
        n, m = m, n
    while m:
        r = n % m
        n, m = m, r

    return n


def solution(w, h):
    # 항상 높이가 더 높도록
    if h < w:
        h, w = w, h

    origin_area = w * h
    gcdd = gcd(w, h)
    sub_area = (w//gcdd + h//gcdd - 1) * (gcd(w, h))

    return origin_area - sub_area

print(solution(8, 12))