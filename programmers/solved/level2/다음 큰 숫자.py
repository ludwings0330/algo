# 다음 큰 숫자
def solution(n):
    answer = 0
    b = str(bin(n)[2:])
    one_counter = b.count("1")

    k = n + 1
    while str(bin(k)[2:]).count("1") != one_counter:
        k += 1
    return k


print(solution(78))
#83

print(solution(15))
# 23
