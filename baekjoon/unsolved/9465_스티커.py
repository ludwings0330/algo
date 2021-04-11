import sys

inp = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(sys.stdin.readline())
        visit = [[False]*N, [False]*N]
        visit[0][2] = True
        sticker = []
        answer = 0

        for j in range(2):
            sticker.append(list(map(int, inp().split())))

        for k in range(0, N-1):
            if sticker[0][k] + sticker[1][k+1] > sticker[1][k] + sticker[0][k+1]:
                if sticker[0][k] >= sticker[1][k+1]:
                    answer += sticker[0][k]
                    visit[0][k] = True
                    visit[1][k] = True
                    visit[0][k+1] = True
                else:
                    answer += sticker[1][k+1]
                    visit[1][k+1] = True
                    visit[0][k+1] = True
                    visit[1][k] = True

            else:
                if sticker[1][k] > sticker[0][k+1]:
                    answer += sticker[1][k]
                    visit[1][k] = True
                    visit[0][k] = True
                    visit[1][k+1] = True
                else:
                    answer += sticker[0][k+1]
                    visit[0][k+1] = True
                    visit[0][k] = True
                    visit[1][k+1] = True

        print(answer)