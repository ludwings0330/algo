if __name__ =="__main__":
    mushroom = []
    result = []

    for i in range(10):
        mushroom.append(int(input()))

    pointSum = []
    for i in range(0, 11):
            pointSum.append(sum(mushroom[0:i]))

    for i in range(11):
        k = abs(100-pointSum[i])
        result.append(k)

    MIN = min(result)
    for i in range(10,-1, -1):
        if result[i] == MIN:
            print(pointSum[i])
            break