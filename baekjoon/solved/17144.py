import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
airPurifier = []
dust_dict = {(r, c):0 for r in range(R) for c in range(C)}

for r in range(R):
    line = (list(map(int, input().split())))
    for c in range(C):
        if line[c] == -1:
            airPurifier.append([r, c])
            dust_dict[(r, c)] = -1
        elif line[c] != 0:
            dust_dict[(r, c)] = line[c]
dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def spreadDust():
    tdust = dict()
    for (r, c), dust in dust_dict.items():
        if dust < 5:
            continue

        n = dust // 5

        for i in range(4):
            tr = r + dd[i][0]
            tc = c + dd[i][1]
            if 0 <= tr < R and 0 <= tc < C and dust_dict[(tr, tc)] != -1:
                dust_dict[(r, c)] -= n
                if (tr, tc) in tdust:
                    tdust[(tr, tc)] += n
                else:
                    tdust[(tr, tc)] = n

    for (r, c), dust in tdust.items():
        dust_dict[(r, c)] += dust

def airPurifierOperation():
    r1, c1 = airPurifier[0]
    r2, c2 = airPurifier[1]
    d1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    d2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    direction = 0
    now = 0
    while True:
        tr1 = r1 + d1[direction][0]
        tc1 = c1 + d1[direction][1]
        if 0 <= tr1 < R and 0 <= tc1 < C:
            r1 = tr1
            c1 = tc1
        else:
            direction += 1
            continue

        next1 = dust_dict[(tr1, tc1)]

        if next1 == -1:
            break

        dust_dict[(tr1, tc1)] = now
        now = next

    direction = 0
    now = 0
    while True:
        tr = r2 + d2[direction][0]
        tc = c2 + d2[direction][1]
        if 0 <= tr < R and 0 <= tc < C:
            r2 = tr
            c2 = tc
        else:
            direction += 1
            continue

        next = dust_dict[(tr, tc)]

        if next == -1:
            break

        dust_dict[(tr, tc)] = now
        now = next

while T:
    T -= 1
    spreadDust()
    airPurifierOperation()
SUM = 2
for n in dust_dict.values():
    SUM += n
print(SUM)