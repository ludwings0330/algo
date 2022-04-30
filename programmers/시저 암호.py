# 문자열 s, 문자를 미는 거리 n
def solution(s, n):
    answer = []
# % end + start
    l = len("qwertyuiopasdfghjklzxcvbnm")
    for c in s:
        start, end = ['a', 'z'] if 'a' <= c <= 'z' else ['A', 'Z']

        trans = chr((ord(c) + n) % ord(start) % l + ord(start))
        if c == ' ':
            trans = c
        answer.append(trans)

    return ''.join(answer)

print(solution("AB", 1))
print(solution("AB", 3))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("abcdefABCDEF", 25))

while True:
    s = input()
    n = int(input())

    print(solution(s, n))