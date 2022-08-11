import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
equation = list(input())
size = (N-1)//2
isSelected = [False] * size
ans = -float('inf')


def calculate():
    tmp = [equation[0]]
    for i in range(size):
        if isSelected[i]:
            tmp.append(str(eval(tmp.pop() + equation[i*2+1] + equation[i*2+2])))
        else:
            tmp.append(equation[i*2+1])
            tmp.append(equation[i*2+2])

    global ans
    tmp.reverse()
    k = int(tmp.pop())
    while tmp:
        e = tmp.pop()
        if e == '*':
            k *= int(tmp.pop())
        elif e == '-':
            k -= int(tmp.pop())
        elif e == '+':
            k += int(tmp.pop())
    ans = max(ans, k)


def subSet(idx):
    if idx >= size:
        calculate()
        return

    isSelected[idx] = True
    subSet(idx+2)
    isSelected[idx] = False
    subSet(idx+1)


subSet(0)
print(ans)