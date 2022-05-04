# 입력이 빈 문자열인 경우 빈 문자열을 반환
from collections import deque


def check_correct(u):
    dq = deque()
    dq.append(u[0])

    for i in range(1, len(u)):
        if not dq:
            break

        if u[i] == ')':
            if dq[-1] == '(':
                dq.pop()
            else:
                dq.append(u[i])
        if u[i] == '(':
            dq.append(u[i])
    return True if not dq else False


def convert(s):
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
    return s

def solution(p):
    if not p:
        return ''

    answer = ''
    p = list(p)
    dq = deque()
    dq.append(p[0])
    u = [p[0]]
    v = []
    for i in range(1, len(p)):
        if not dq:
            v = p[i:]
            break
        if p[i] != dq[-1]:
            dq.pop()
        else:
            dq.append(p[i])
        u.append(p[i])

    print(u, v)

    if check_correct(u):
        answer = ''.join(u) + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = convert(u[1:-1])
        answer += ''.join(u)

    return answer
# 괄호가 개수는 맞지만 짝이 맞지 않음
# 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괋호 문자열을 알려주는 프로그램 개발

# 균형잡힌 괄호 문자열 (, ) 로만이루어지고, 개수가 서로 같다면
# (, ) 의 짝이 맞다면 올바른 괄호 문자열

# 균형잡힌 괄호 문자열이 주어질때 올바른 괄호 문자열로 변환한 결과를 return
pp = ["(()())()", ")(", "()))((()"]
for p in pp:
    print(solution(p))
