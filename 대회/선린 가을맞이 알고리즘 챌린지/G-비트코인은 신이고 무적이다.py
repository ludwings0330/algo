import sys
input = lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())

'''
이전 N개의 월봉을 통해 다음 월봉의 절댓값을 예측
다음 월봉의 절대값 = N개의 월봉중 중복을 허용해 M 개를 골라서 절대 값들을 bitwise xor

1의 갯수
    홀수면 1
    짝수면 0
    
find(n, m) : n번째 월봉을 뽑을 때 남은 갯수 m 개 뽑을 때 최대값 반환

'''

A = list(map(int, input().split()))
A = list(map(abs, A))
A.sort(reverse=True)
cache = [[-1] * (M+1) for _ in range(N)]

def find(n, m):
    if m == 0:
        return 0
    if n == N-1:
        # 마지막까지 왔을때는 경우를 잴 필요없이 남은 회수 모두 소모한다.
        return xor(A[n], A[n], m)

    if cache[n][m] != -1:
        return cache[n][m]

    cache[n][m] = 0
    for i in range(m+1):
        cache[n][m] = max(cache[n][m], xor(xor(A[n], A[n], i), find(n+1, m-i), 1))

    return cache[n][m]

def xor(num1, num2, k):
    if num1 == num2:
        if k % 2 == 0:
            return 0
        else:
            return num1

    for _ in range(k):
        num1 = num1 ^ num2

    return num1

print(find(0, M))