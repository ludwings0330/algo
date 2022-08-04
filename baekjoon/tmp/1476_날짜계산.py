yr, E, S, M = 1, 1, 1, 1

target = list(map(int, input().split()))

while [E, S, M] != target:
    yr += 1
    E = max(1, (E+1) % 16)
    S = max(1, (S+1) % 29)
    M = max(1, (M+1) % 20)

print(yr)