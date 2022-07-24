import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

W = int(input())
dict_count = defaultdict(int)
MAX = 0

for w in range(1, W+1):
    rooms = [''] * 200

    for i in range(20):
        room, name = input().split()
        room = int(room)
        rooms[room] = name

    for d in range(5):
        is_odd, divisor, first_name = input().split()

        for i in range(101, 121):
            if i % 2 == 1 and is_odd == 'O':
                continue
            elif i % 2 == 0 and is_odd == 'E':
                continue
            if i % int(divisor) == 0:
                continue
            if rooms[i].lower()[0] == first_name.lower():
                continue

            dict_count[rooms[i]] += 1
            MAX = max(MAX, dict_count[rooms[i]])

    print(f'WEEK {w}')
    for i in range(101, 121):
        if dict_count[rooms[i]] == MAX:
            print(rooms[i])
