W, H = map(int, input().split())
N = int(input())
w = [0, W]
h = [0, H]
for _ in range(N):
    d, pos = map(int, input().split())
    # d == 0 가로, d == 1 세로
    if d == 0:
        h.append(pos)
    else:
        w.append(pos)

w.sort()
h.sort()

l_w = []
l_h = []
for i in range(1, len(w)):
    l_w.append(w[i] - w[i-1])
for i in range(1, len(h)):
    l_h.append(h[i] - h[i-1])

answer = 0
for ww in l_w:
    for hh in l_h:
        answer = max(answer, ww*hh)
print(answer)
