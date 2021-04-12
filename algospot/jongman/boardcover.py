if __name__ == "__main__":
    C = int(input())
    dType = [[[0, 0], [1, 0], [0, 1]],[[0, 0], [0, 1], [1, 1]], [[0,0], [1, 0], [1, 1]], [[0, 0], [0, 1], [-1, 1]]]

    def checkType(x, y, Type, iboardList):
        ret = True
        for i in range(len(dType[Type])):
            tx = x + dType[Type][i][0]
            ty = y + dType[Type][i][1]
            if not 0 <= tx < W or not 0 <= ty < H or iboardList[ty][tx] != '.':
                ret = False
                break

        return ret

    def recursiveCheck(iboardList):
        finished = True
        x = y = -1

        for i in range(H):
            if not finished:
                break
            for j in range(W):
                if iboardList[i][j] == '.':
                    finished = False
                    x, y = j, i
                    break

        if finished:
            return 1

        ret = 0

        for Type in range(len(dType)):
            if checkType(x, y, Type, iboardList):
                for i in range(len(dType[Type])):
                    tx = x + dType[Type][i][0]
                    ty = y + dType[Type][i][1]
                    iboardList[ty][tx] = 'B'
                ret += recursiveCheck(iboardList)
                for i in range(len(dType[Type])):
                    tx = x + dType[Type][i][0]
                    ty = y + dType[Type][i][1]
                    iboardList[ty][tx] = '.'

        return ret

    while C:
        C -= 1
        H, W = map(int, input().split())
        boardList = []
        for i in range(H):
            boardList.append(list(input()))

        answer = recursiveCheck(boardList)
        print(answer)