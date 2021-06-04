N = int(input())
c = 0
for i in range(1334):
    f = False
    for j in range(1001):
        if N == 5*j + 3*i:
            print(j+i)
            f = True
            break
    if f:
        break
else:
    print(-1)