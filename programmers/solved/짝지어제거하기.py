def solution(s):
    answer = 0
    stack = []

    for ch in list(s):
        if len(stack) == 0:
            stack.append(ch)
        else:
            if stack[len(stack)-1] == ch:
                stack.pop()
                continue
            else:
                stack.append(ch)
    if len(stack) == 0:
        answer = 1
        
    return answer

if __name__ == "__main__":
    s = 'baab'
    print("answer is {}".format(solution(s)))