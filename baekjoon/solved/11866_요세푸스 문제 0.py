if __name__ == "__main__":
    N, K = map(int, input().split())
    numList = [i+1 for i in range(0, N)]
    index = 0
    answer = []
    while len(numList) > 0:
        index = (index+K-1)%len(numList)
        answer.append(numList[index])
        del numList[index]

    answer = ', '.join(map(str, answer))
    print('<'+answer+'>')