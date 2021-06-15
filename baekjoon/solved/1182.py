# 부분수열의 합
# 1<= N <= 20
# 부분 수열의 원소를 다더한 값이 S가 되는 경우의 수 구하기
import sys
input = sys.stdin.readline

N, S = map(int,input().split())
l = list(map(int, input().split()))
cnt = 0

def recursiveSolve(i, SUM):
    if i == N:
        return
    if SUM+l[i] == S:
        global cnt
        cnt += 1

    recursiveSolve(i+1, SUM + l[i]) #더하거나
    recursiveSolve(i+1, SUM) # 더하지않거나

recursiveSolve(0, 0)
# N 이 20 선택하거나 선택하지 않거나 2^20이 백만정도니까 충분히가능하다
print(cnt)