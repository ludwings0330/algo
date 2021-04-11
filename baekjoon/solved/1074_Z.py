import sys
import copy
sys.setrecursionlimit(10000)

if __name__ == "__main__":
    N, r, c = map(int, input().split())
    # 2^N x 2^N 의 행렬 Z 탐색
    # r:y행 c:x열에 몇 번째로 방문하는지 출력.
    # 2x2 쪼개고 쪼개서 최소가 2x2
    start = [0, 0]
    end = [2 ** N - 1, 2 ** N - 1]
    answer = 0


    def solution(n, s, e):
        global answer

        if s[1] == r and s[0] == c:
            print(int(answer))
            return

        if n == 1:
            return

        if s[1] <= r <= e[1]-n//2 and s[0] <= c <= e[0]-n//2:
            #answer += (n//2) * (n//2)
            solution(n//2, s, [e[0]-n//2, e[1]-n//2])
        elif s[1] <= r <= e[1] - n//2 and s[0]+n//2 <= c <= e[0]:
            answer += (n//2) * (n//2)
            solution(n//2, [s[0]+n//2, s[1]], [e[0], e[1]-n//2])
        elif s[1]+n//2 <= r <= e[1] and s[0] <= c <= e[0] - n//2:
            answer += ((n//2) * (n//2)) *2
            solution(n//2, [s[0], s[1]+n//2], [e[0]-n//2, e[1]])
        else:
            answer += ((n//2) * (n//2)) *3
            solution(n//2, [s[0]+n//2, s[1]+n//2], e)


    solution(2 ** N, start, end)