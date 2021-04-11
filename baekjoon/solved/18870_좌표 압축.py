import sys
if __name__ == "__main__":
    N = int(input())
    numList = (list(map(int , input().split())))
    setNumList = set(numList)
    sortedNumList = sorted(setNumList)
    dic = {}

    for i in range(len(sortedNumList)):
        if sortedNumList[i] not in dic:
            dic[sortedNumList[i]] = i
    for num in numList:
        sys.stdout.write(str(dic[num])+' ')