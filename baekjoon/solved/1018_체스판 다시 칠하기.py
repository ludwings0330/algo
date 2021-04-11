if __name__ == "__main__":
    # N 행 M 열
    N, M = map(int, input().split())
    chess = []
    color = ['W', 'B']

    for i in range(N):
        chess.append(list(input()))
    MIN = int(8*8/2)

    for i in range(N):
        if i+8 > N:
            break
        for j in range(M):
            if j+8 > M:
                break
            for c in color:
                index = color.index(c)
                count = 0
                for ty in range(i, i+8):
                    for tx in range(j, j+8):
                        if chess[ty][tx] != color[index]:
                            count += 1
                        index = (index+1)%2
                    index = (index+1)%2
                if count < MIN:
                    MIN = count

    print(MIN)