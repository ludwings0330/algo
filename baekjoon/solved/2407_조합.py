N, M = map(int, input().split())

#nCm 출력
answer = 1
for i in range(M):
    answer *= (N-i)

for i in range(M):
    answer //= (M-i)
print(answer)