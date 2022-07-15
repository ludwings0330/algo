t = int(input())
test_case = 1

while t:
    t -= 1
    ans = 0
    N = int(input())

    for i in range(1, N+1):
        if i%2 == 1:
            ans += i
        else:
            ans -= i

    print(f'#{test_case} {ans}')
    test_case += 1
