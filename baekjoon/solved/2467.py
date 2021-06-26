import sys
input = sys.stdin.readline

MIN = 9876543212

N = int(input())

liquids = list(map(int, input().split()))
liquids.sort()

s, e = 0, N -1
while s < e:
    NOW = liquids[s] + liquids[e]
    if MIN > abs(NOW):
        MIN = abs(NOW)
        answer = [liquids[s], liquids[e]]
    if NOW < 0:
        s += 1
    elif NOW > 0:
        e -= 1
    else:
        answer = [liquids[s], liquids[e]]
        break

print(' '.join( str(s) for s in answer))