TC = int(input())


def check():
    pass

# 부분 문제 정의
# build(n, l, r) :  n번 건물을 설치할 차례고 왼쪽에서 보이는 건물의 수가 l, 오른쪽에서 보이는 건물의 수가 r개가 되도록 건설할 수 있는 경우의 수 return
def build(n, l, r):
    if n == 0:
        if l == 0 and r == 0:
            return 1
        else:
            return 0

    if cache[n][l][r] != -1:
        return cache[n][l][r]

    cache[n][l][r] = 0
    # 1. 왼쪽에 추가적으로 보이게 건설 할 수 있다.
    if l-1 >= 0:
        cache[n][l][r] += build(n-1, l-1, r)

    # 2. 오른쪽에 추가적으로 보이게 건설 할 수 있다.
    if r-1 >= 0:
        cache[n][l][r] += build(n-1, l, r-1)

    # 3. 왼쪽 오른쪽 둘다 안보이게 건물들 사이에 건설할 수 있다. 이 경우, 건물을 지을 수 있는 위치는 왼쪽 오른쪽 두개  제외하고 사이사이에 들어갈 수 있다.
    cache[n][l][r] += (build(n-1, l, r) * ((N-n)-1))

    return cache[n][l][r]


for testCase in range(1, TC+1):
    N, L, R = map(int, input().split())
    # 전체 N 개 높이 1, 2, 3, 4, 5, ,,, N
    # 왼쪽에서 보면 L개 , 오른쪽에서 보면 R 개
    # 가능한 막대의 배치 수 최대 20개
    cache = [[[-1] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

    print("#%d %d" %(testCase, build(N-1, L-1, R-1)))
