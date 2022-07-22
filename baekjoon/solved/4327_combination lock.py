while True:
    d = list(map(int ,input().split()))
    if sum(d) == 0:
        break
    count = 120
    count += (d[0] - d[1] + 40) % 40
    count += (d[2] - d[1] + 40) % 40
    count += (d[2] - d[3] + 40) % 40
    print(count*9)