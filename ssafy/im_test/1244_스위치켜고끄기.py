N = int(input())
switches = [-1] + list(map(int, input().split()))

M = int(input())
for _ in range(M):
    s, number = map(int, input().split())
    if s == 1:
        tmp = number
        while tmp <= N:
            switches[tmp] = (switches[tmp] + 1) % 2
            tmp += number

    elif s == 2:
        k = 0
        while number + k <= N and number - k > 0 and \
                switches[number+k] == switches[number-k]:
            k += 1
        k -= 1
        for i in range(number-k, number+k+1):
            switches[i] = (switches[i] + 1) % 2

for i in range(1, len(switches)):
    print(switches[i], end =' ')
    if i % 20 == 0:
        print('')
