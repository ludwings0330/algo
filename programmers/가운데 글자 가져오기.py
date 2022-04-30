def solution(s):
    l = len(s)
    return s[l//2:l//2+1] if l % 2 == 1 else s[l//2-1:l//2+1]


s = ["abcde", "qwer"]

for i in range(len(s)):
    print(solution(s[i]))