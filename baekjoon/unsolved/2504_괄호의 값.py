
def check():
    stack = []
    ret = True

    if len(inputString) %2 != 0: #무조건 짝수여야 올바른거지
        ret = False

    for ch in list(inputString):
        if ch != '(' and ch != '[' and ch != ')' and ch != ']':
            ret = False

        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ']':
            if len(stack) == 0 or stack.pop() != '[':
                ret = False
        elif ch == ')':
            if len(stack) == 0 or stack.pop() != '(':
                ret = False
    if len(stack) != 0:
        ret = False

    return ret

def recursiveSolve(stack, index):
    if index >= len(inputString) - 1:
        return 0

    ret = 1
    if inputString[index] == ')' or inputString[index] == ']':
        stack.pop()
        return recursiveSolve(stack, index+1)

    if inputString[index] == '(':
        if inputString[index+1] == ')':
            ret = ret*2 + recursiveSolve(stack, index+2)
        else:
            stack.append(inputString[index])
            ret = ret*2 * recursiveSolve(stack, index+1)

    elif inputString[index] == '[':
        if inputString[index+1] == ']':
            ret = ret*3 + recursiveSolve(stack, index+2)
        else:
            stack.append(inputString[index])
            ret = ret*3 * recursiveSolve(stack, index+1)
    return ret

inputString = input().strip()

if check():
    print(recursiveSolve([], 0))
else:
    print(0)