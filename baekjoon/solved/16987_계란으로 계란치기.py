import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = [0] * (N+1)
W = [0] * (N+1)

for i in range(1, N+1):
    # 계란의 내구도와 무게를 초기화 합니다. 편의상 계란의 번호는 1에서 N으로 설정했습니다.
    s, w = map(int, input().split())
    S[i] = s
    W[i] = w


def recursive(i):
    ret = 0
    # base case N+1 번째 계란은 없습니다
    if i == N+1:
        # 모든 계란이 깨져있는지 확인합니다.
        for j in range(1, N+1):
            if S[j] <= 0:
                ret += 1
        return ret

    # 손에 쥔 계란이 이미 깨져있다면 다음 단계로 넘어갑니다.
    if S[i] <= 0:
        return recursive(i+1)

    flag = False

    # i 번째 계란과 k 번째 계란을 부딪힙니다.
    for k in range(1, N+1):
        if i == k:
            continue
        # k 번째 계란이 아직 깨지지 않았다면 두 계란을 부딪힌 후 다음 단계로 진행합니다.
        if S[k] > 0:
            flag = True
            # 계란이 서로 부딪히며 내구도가 감소합니다
            S[i] -= W[k]
            S[k] -= W[i]

            # 계란을 부딪혔으니, 다음 단계로 진행합니다.
            ret = max(ret, recursive(i+1))

            # 계란의 내구도를 복원합니다.
            S[i] += W[k]
            S[k] += W[i]

    if not flag:
        return recursive(i+1)

    return ret


print(recursive(1))