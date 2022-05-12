def solution(dirs):
    answer = 0
    move = {'U':(1, 0), 'D':(-1, 0), 'R':(0, 1), 'L':(0, -1)}
    visit = set()
    cx, cy = 0, 0

    for direction in dirs:
        dy, dx = move[direction]
        nx = cx + dx
        ny = cy + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visit.add((cy, cx, ny, nx))
            visit.add((ny, nx, cy, cx))
            cx = nx
            cy = ny
    return len(visit)//2

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LLLLLLLLLLLLLLLLLLLLLLRRRR"))
