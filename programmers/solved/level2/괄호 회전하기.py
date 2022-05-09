start = list("([{")
end = list(")]}")

def isCorrect(s):
    stack = []
    ret = True

    for c in s:
        if not stack:
            stack.append(c)
            continue
        if c in start:
            stack.append(c)
        else:
            if (c == ')' and stack[-1] != '(') or (c == ']' and stack[-1] != '[') or (c == '}' and stack[-1] != '{'):
                ret = False
                break
            else:
                stack.pop()
    if stack:
        ret = False
    return ret

def solution(s):
    answer = 0

    for x in range(0, len(s)):
        answer += 1 if isCorrect(s[x:] + s[0:x]) else 0

    return answer


ss = ["[](){}", "}]()[{", "[)(]", "}}}"]

for s in ss:
    print(solution(s))
