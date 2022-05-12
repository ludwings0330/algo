import re


def solution(s):
    answer = []
    conversion_counter = 0
    zero_counter = 0

    while s != "1":
        conversion_counter += 1
        zero_counter += s.count('0')
        s = re.sub('[0]', '', s)

        n = len(s)
        tmp = []
        while n:
            tmp.append(str(n%2))
            n //= 2
        s = ''.join(map(str, tmp))

    return [conversion_counter, zero_counter]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))