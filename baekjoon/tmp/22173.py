r, b = map(int, input().split())
count_r = 0
count_b = 1
move = 0
ans = []

# color == 1 : current color red
# color == 0 : current color black
color = 0

while count_b <= b and count_r <= r:
    ans.append('E')
    ans.append('E')
    move += 2
    color = (color + 1) % 2
    if color:
        count_r += 1
    else:
        count_b += 1
ans.pop()
ans.pop()
move -= 2

if color:
    count_r -= 1
else:
    count_b -= 1

moves = [list('SEEN'), list('ESSW')]
count = 0
while count < abs(r + b - (count_r + count_b)):
    ans.extend(moves[count%2])
    count += 1
    move += 4

ans = ''.join(ans)
print(move)
if move:
    print(ans)
