t = int(input())
test_case = 1

while t:
    t -= 1
    a, b = map(int, input().split())

    print(f'#{test_case} {a//b} {a%b}')
    test_case += 1