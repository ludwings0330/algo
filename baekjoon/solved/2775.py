T = int(input())
while T:
    T -= 1
    k = int(input())
    n = int(input())
    # k층 n 호에 몇명이나 살고 있을까?
    room = [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(1, len(room)):
            room[i] = room[i-1]+room[i]
    print(room[n-1])
