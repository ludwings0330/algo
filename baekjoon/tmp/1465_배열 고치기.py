N, low, high = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if low <= A[i] <= high:
        print(A[i], end= ' ')
    elif A[i] < low:
        k = 0
        tmp = A[i]
        while tmp:
            tmp //= 2
            k += 1

        while A[i] + 2 ** k < low:
            k += 1
            

    elif high < A[i]:
        pass
