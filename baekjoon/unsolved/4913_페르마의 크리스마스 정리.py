import sys
input = lambda: sys.stdin.readline().rstrip()

isPrime = [1] * 1_000_001
isPrime[0] = isPrime[1] = 0
primeNumbers = []

for i in range(2, len(isPrime)):
    if isPrime[i] == 0:
        continue
    k = 2

    if (i - 1) % 4 == 0:
        isPrime[i] = 2

    primeNumbers.append((i, isPrime[i]))

    while i * k < len(isPrime):
        isPrime[i * k] = 0
        k += 1

while True:
    L, U = map(int, input().split())
    if L == U == -1:
        break
    _L = L if L > 0 else -L
    x = 0
    y = 0
    for prime in primeNumbers:
        if prime[0] < _L:
            continue
        if prime[0] > U:
            break
        x += 1
        if prime[1] == 2 and L > 0:
            y += 1
    print(L, U, x, y)


