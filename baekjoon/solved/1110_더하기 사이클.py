def Cycle(X, Y):
    answer = X*10 + Y
    cycle = 1
    while True:
        tx = (X+Y)//10
        ty = (X+Y)%10
        newNum = Y*10 + ty
        if newNum == answer:
            return cycle
        cycle += 1
        X = Y
        Y = ty

if __name__ == "__main__":
    N = int(input())
    if N<10:
        print(Cycle(0, N))
    else:
        print(Cycle(N//10, N%10))