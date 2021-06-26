N = int(input())
# 1<= N <= 100

trunkList = [[_] for _ in range(1, N+1)]
trunkList.append([])
trunkList.append([])

def move(N, start, to):
    print(start, to)

def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)
if N <= 20:
    print(2**N-1)
    hanoi(N, 1, 3, 2)
else:
    print(2**N -1)
