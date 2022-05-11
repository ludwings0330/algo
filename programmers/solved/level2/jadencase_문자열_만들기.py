def solution(s):
    s_list = list(s.lower())

    toggle = True
    for i, c in enumerate(s_list):
        if c == ' ':
            toggle = True
            continue

        if toggle:
            if c.isalpha():
                s_list[i] = c.upper()
            toggle = False


    return ''.join(s_list)


# 모듬 단어의 천 문자가 대문자.  그 이외의 알파벳은 소문자

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("123 t2he l4ast 3week"))
print(solution("for the last week "))
