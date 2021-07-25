import sys
input = sys.stdin.readline
p = 1000000007
mat = [[1,1],[1,0]]
sys.setrecursionlimit(10000000)
def go(A, B):
    a = A[0][0]*B[0][0] + A[0][1]*B[1][0]
    b = A[0][0]*B[0][1] + A[0][1]*B[1][1]
    c = A[1][0]*B[0][0] + A[1][1]*B[1][0]
    d = A[1][0]*B[0][1] + A[1][1]*B[1][1]
    temp = [[0,0],[0,0]]
    temp[0][0] = a%p
    temp[0][1] = b%p
    temp[1][0] = c%p
    temp[1][1] = d%p # 여기가 문제였다. 큰수를 꼐속 끌고가면 당연히 오래 걸릴수 밖에 없다.

    return temp

def power(mat, n): # mat 의 n 승을 구하세요
    if n == 1:
         return mat

    elif n%2:
        return go(power(mat, n-1), mat)
    else:
        return power(go(mat, mat), n//2)

def fibo(n):
    if n < 3 :
        return 1
    else:
        answer = power(mat, n-1)
        return answer[0][0]

n = int(input())
print(fibo(n))