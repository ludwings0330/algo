t = int(input())
test_case = 1
while t:
    t -= 1
    ans = 1

    word = list(input())
    reversed_word = word[::-1]
    for i in range(len(word)):
        if word[i] != reversed_word[i]:
            ans = 0
            break

    print(f'#{test_case} {ans}')
    test_case += 1
