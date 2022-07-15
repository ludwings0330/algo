import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

while t:
    t -= 1
    n = int(input())
    number = list(input())
    answer = [str(9 - int(number[i])) for i in range(n)]

    if answer[0] == '0':
        for i in range(n-1, -1, -1):
            tmp = 1
            if i == n-1:
                tmp = 2
            answer[i] = str(int(answer[i]) + tmp)
            if int(answer[i]) >= 10 and i != 0:
                answer[i-1], answer[i] = str(int(answer[i-1]) + (int(answer[i]) // 10)), str(int(answer[i]) % 10)

    print(''.join(answer))
