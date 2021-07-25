N = int(input())

A = [1 for i in range(10)]
A[0] = 0

N -= 1
while N:
    tA = [0 for i in range(10)]
    N -= 1
    for i in range(10):
        if i+1 < 10:
            tA[i+1] += A[i]
        if 0 <= i - 1:
            tA[i-1] += A[i]
    A = tA[:]
print(sum(A)%1000000000)