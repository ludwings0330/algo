import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dices = []

for _ in range(N):
    A, B, C, D, E, F = map(int, input().split())
    dices.append([A, F, B, D, C, E])
    # idx // 2 *b 2, idx // 2 * 2 + 1 는 같은 그룹

max_value = 0

for i in range(6):
    top = dices[0][i] # 맨 윗면의 숫자
    total = max(dices[0][:i//2*2]+dices[0][i//2*2+2:])
    for j in range(1, N):
        for k in range(6):
            if top == dices[j][k]:
                top = dices[j][k + 1 if k % 2 == 0 else k-1]
                total += max(dices[j][:k//2*2]+dices[j][k//2*2+2:])
                break
    max_value = max(max_value, total)
print(max_value)
