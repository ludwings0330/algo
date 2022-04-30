# p와 y의 갯수가 같으면 True 다르면 False
def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


print(solution("pPoooyY"))
print(solution("Pyy"))