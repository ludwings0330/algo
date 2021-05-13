inputString = input()

stack = []
stackIndex = []
answer = []
answer2 = set()
flag = True

for i in range(len(inputString)):
    ch = inputString[i]
    if ch == '(':
        stack.append(ch)
        stackIndex.append(i)
    elif ch == ')':
        if len(stack) != 0:
            ch2 = stack.pop()
            if ch2 == '(':
                answer.append([stackIndex.pop(), i])
        else:
            break

visit = [False] * len(answer)


def Solve(remains, k):

    if remains == 0:
        # print
        tmp = list(inputString)
        for i in range(len(visit)):

            if visit[i]:  # 방문했으면
                p, q = answer[i]
                tmp[p] = tmp[q] = ''
        answer2.add(''.join(tmp))
        return

    for i in range(k, len(visit)):
        if not visit[i]:
            visit[i] = True
            Solve(remains - 1, i)
            visit[i] = False


for k in range(1, len(answer) + 1):
    Solve(k, 0)

for strs in sorted(answer2):
    print(strs)
