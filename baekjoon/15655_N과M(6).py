import sys
input = lambda: sys.stdin.readline().rstrip()


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

'''
길이가 M인 오름차순이 되는 수열 모두 출력하기
'''

visit = [False] * N
def print_ans():
    for i in range(N):
        if visit[i]:
            print(A[i], end=' ')
    print()

def recursiveSolve(toPick, idx):
    if toPick == 0:
        print_ans()

    for i in range(idx+1, N):
        visit[i] = True
        recursiveSolve(toPick-1, i)
        visit[i] = False


recursiveSolve(M, -1)
