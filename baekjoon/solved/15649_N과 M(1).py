
if __name__ == "__main__":
    N, M = map(int, input().split())

    # 1 ~ N 까지 자연수 중에서
    # M개를 고르는 경우의 수.
    visit = [False] * (N+1)
    def solution(visit, c):
        if len(c) >= M:
            print(' '.join(map(str, c)))
            return
        for i in range(1, N+1):
            if i not in c:
                solution(visit[:], c+[i])

    solution(visit, [])