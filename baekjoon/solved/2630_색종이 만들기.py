import sys

if __name__ == "__main__":
    K = int(input())
    paper = []
    answer = [0, 0]
    for i in range(K):
        paper.append(list(map(int, sys.stdin.readline().split())))

    def solution(x, y, k):
        flag = False
        stand = paper[y][x]
        if k == 1:
            if paper[y][x] == 1:
                # 파란색
                answer[1] += 1
                return 1
            else: # 하얀색
                answer[0] += 1
                return 0

        for i in range(y,y+k):
            if flag:
                break
            for j in range(x,x+k):
                if paper[i][j] != stand:
                    flag = True
                    break

        if not flag:# 모두 같으면
            if paper[y][x] == 1: # 파란색으로 모두 같으면
                answer[1] += 1
                return 1
            else:
                answer[0] += 1
                return 0
        else:
            solution(x,y,k//2)
            solution(x, y+k//2, k//2)
            solution(x+k//2, y, k//2)
            solution(x+k//2, y+k//2, k//2)


    solution(0, 0, K)
    print(answer[0], answer[1],sep='\n')
