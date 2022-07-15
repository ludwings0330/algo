k = int(input())
for i in range(1, k+1):
    tmp = i
    count = 0
    while tmp > 0:
        if tmp % 10 in [3, 6, 9]:
            count += 1
        tmp //= 10
    if count == 0:
        print(i, end=' ')
    else:
        print('짝'*count, end=' ')