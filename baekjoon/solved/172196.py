import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
for i in range(N):
    key, item = input().split()
    dic[key] = item

for i in range(M):
    key = input().rstrip()
    print(dic[key])