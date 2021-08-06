def getinverse(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b

    if n % 2 == 1:
        a = getinverse(b, n // 2)
        c = a * b
        return a * c
    else:
        a = getinverse(b, n // 2)
        return a * a
for i in range(10):
    print(getinverse(3, i))