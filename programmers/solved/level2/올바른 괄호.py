def solution(s):
    answer = True
    stack = []
    for c in s:
        if stack and c == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    return len(stack) == 0

