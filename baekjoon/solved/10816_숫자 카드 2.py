if __name__=="__main__":
    N = int(input())
    nList = list(map(int, input().split()))
    M = int(input())
    mList = list(map(int, input().split()))
    dic = dict()

    for card in nList:
        if card not in dic:
            # 존재하지 않으면
            dic[card] = 1
        else:
            dic[card] += 1
    for card in mList:
        if card in dic:
            print(dic[card], end=' ')
        else:
            print(0, end=' ')

