t = int(input())

test_case = 1
while t:
    t -= 1

    answer = ''

    a, b = map(int, input().split())
    if a < b:
        answer = '<'
    elif a > b:
        answer = '>'
    else:
        answer = '='

    print(f'#{test_case} {answer}')
    test_case += 1