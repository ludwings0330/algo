import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
liquids = []
gas = []
for _ in range(n):
    a, b = map(int, input().split())
    liquids.append(a)
    gas.append(b)

M = int(input())

hasChanged = True

max_gas = max(gas)
while M:
    hasChanged = False
    next_max_gas = max_gas
    for i in range(n):
        if gas[i] < max_gas:
            hasChanged = True
            gas[i] += liquids[i]
            M -= 1
            next_max_gas = max(next_max_gas, gas[i])
    max_gas = next_max_gas

    if not hasChanged and M > 0:
        gas[0] += liquids[0]
        M -= 1
        max_gas = gas[0]

print(gas[0] if len(set(gas)) == 1 else 0)
