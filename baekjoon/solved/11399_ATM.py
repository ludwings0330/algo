import sys

if __name__ == "__main__":
    N = int(input())
    numList = list(map(int, input().split()))

    numList.sort()

    for i in range(1, len(numList)):
        numList[i] = numList[i] + numList[i-1]

    print(sum(numList))