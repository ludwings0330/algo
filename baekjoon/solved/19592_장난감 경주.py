# N 명 참가자
# X 트랙 길이
# 속도 V[i] m/s
# 부스터 X 이후로 V[N]
# 부스터 한계치 Y
# 처음 1초간 부스터 Z m/s
# Z<=Y
# 이때 단독우승 최소 Z 값.
# 부스터를 쓰지 않고도 단독 우승 = 0
# 부스터 최대치로 쓰고도 단독우승 불가능 = -1
def Race(N, X, Y, V):
    goalTime = []
    for i in range(N):
        goalTime.append(X/V[i])
    if min(goalTime) == goalTime[N-1] and goalTime.index(min(goalTime)) == N-1:
        # 부스터를 쓰지 않았는데 단독 우승.
        return 0
    if min(goalTime) <= (X-Y)/V[N-1]+1:
        # 부스터 최대로 썻느데 단독우승 불가능
        return -1
    Z = V[N-1]

    while True:
        goalTime[N-1] = (X-Z)/V[N-1]+1
        if min(goalTime) == goalTime[N - 1] and goalTime.index(min(goalTime)) == N - 1:
            # 부스터를 쓰지 않았는데 단독 우승.
            Z = Z-1
            goalTime[N - 1] = (X - Z) / V[N - 1] + 1
            if min(goalTime) == goalTime[N - 1] and goalTime.index(min(goalTime)) == N - 1:
                # 하나 줄였는 데도 단독우승이면 최소값이 아니야.
                Y = Z
            else: # 하나 줄였더니 단독우승아니면
                return Z+1

        Z = (Y+Z)//2

if __name__ == "__main__":
    T = int(input()) # 테스트 케이스
    testCase = []
    for i in range(T):
        N, X, Y = map(int, input().split())
        V = (list(map(int, input().split())))

        print(Race(N,X,Y,V))