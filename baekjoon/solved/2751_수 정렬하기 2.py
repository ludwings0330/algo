import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [int(input()) for i in range(N)]

def mergeSort(A):
    # base Case
    # 더 이상 분해할 수 없으면 List A 를 반환한다.

    if len(A) == 1:
        return A

    # 우선 끝까지 분할해줘야한다.
    left = mergeSort(A[:len(A)//2])
    right = mergeSort(A[len(A)//2:])

    # left, right 는 이미 정렬된 상태로 들어와야 하므로, 이 아래에서 정렬해준다.
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            A[k] = left[l]
            l += 1
        else:
            A[k] = right[r]
            r += 1
        k += 1
    if l == len(left):
        while r < len(right):
            A[k] = right[r]
            r += 1
            k += 1
    elif r == len(right):
        while l < len(left):
            A[k] = left[l]
            l += 1
            k += 1

    return A


S = mergeSort(S)

for ss in S:
    print(ss)