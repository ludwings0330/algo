import sys

if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1
        N = int(input())
        numList = []

        for i in range(2):
            numList.append(list(map(int, input().split())))
        if N == 1:
            print(*max(numList[0], numList[1]))
            continue
            
        numList[0][1] += numList[1][0]
        numList[1][1] += numList[0][0]

        for i in range(2, N):
            numList[0][i] += max(numList[1][i-1], numList[1][i-2])
            numList[1][i] += max(numList[0][i-1], numList[0][i-2])

        print(max(numList[0][-1], numList[1][-1]))