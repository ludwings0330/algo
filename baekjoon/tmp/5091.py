import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

W = int(input())

for w in range(1, W+1):
    rooms = [''] * 200
    count = [0] * 200
    MAX = 0

    for i in range(20):
        room, name = input().split()
        room = int(room)
        rooms[room] = name

    for d in range(5):
        is_odd, divisor, first_name = input().split()

        for i in range(101, 121):
            if i % 2 == 1 and is_odd == 'O':
                continue
            if i % 2 == 0 and is_odd == 'E':
                continue
            if i % int(divisor) == 0:
                continue
            if rooms[i].lower()[0] == first_name.lower():
                continue

            count[i] += 1
            MAX = max(MAX, count[i])

    print(f'WEEK {w}')
    for i in range(101, 121):
        if count[i] == MAX and count[i] != 0:
            print(rooms[i])
