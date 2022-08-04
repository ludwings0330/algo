k = int(input())

# k 번째에 오는 문자를 출력하라.
# 1 <= k <= 10**18

def solution(n, count):
    if n == 1:
        if count % 2 == 1:
            return "1"
        else:
            return "0"

    tmp = 0
    while n - 2**tmp > 0:
        tmp += 1
    return solution(n - 2**(tmp - 1), count + 1)

print(solution(k, 0))