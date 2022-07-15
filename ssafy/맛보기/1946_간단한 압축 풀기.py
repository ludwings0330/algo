t = int(input())
test_case = 1
while t:
    t -= 1

    k = int(input())
    ans = []
    for i in range(k):
        s, k = input().split()
        k = int(k)
        ans.extend([s] * k)
    print(f'#{test_case}')
    test_case += 1
    for i in range(len(ans)):
        print(ans[i], end='')
        if i % 10 == 9:
            print()
    print()