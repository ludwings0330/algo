T = int(input())

while T:
    T -= 1
    N = int(input())
    a = 3
    for n in range(3, N+1):
        a = 2 * a + (n+1) * pow(2, n-2)
    print((a / pow(2, N-1)))
