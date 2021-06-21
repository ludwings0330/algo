import sys
input = sys.stdin.readline

while True:
    s = input()
    isBalanced = True

    if s == ".\n":
        break

    stack = []
    for ch in s:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == ']':
            if stack:
                compareCh = stack.pop()
                if ch == ')' and compareCh != '(':
                    isBalanced = False
                elif ch == ']' and compareCh !='[':
                    isBalanced = False
            else:
                isBalanced = False

        if not isBalanced:
            break

    if isBalanced and not stack:
        print('yes')
    else:
        print('no')