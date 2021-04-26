if __name__ == "__main__":
    fiboList = [0, 1]
    N = int(input())
    if N == 0 or N == 1:
        print(fiboList[N])
    else:
        for i in range(2, N+1):
            fiboList.append(fiboList[i-2]+fiboList[i-1])
        print(fiboList[-1])