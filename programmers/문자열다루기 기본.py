# 길이가 4~6 숫로만 구성되면 True 아니면 False

def solution(s):
    answer = True
    if not (len(s) == 4 or len(S) == 6):
        answer = False

    if not s.isdigit():
        answer = False

    return answer
