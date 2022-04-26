# 1 <= N <= 500 : 스테이지 갯수
# 1 <= stages[i] <= N + 1 : 사용자가 멈춰 있는 스테이
# 1 <= len(stages) <= 200,000
def solution(N, stages):
    max_stage = N + 2

    total = [0] * max_stage
    fail = [0] * max_stage
    for stage in stages:
        for i in range(stage+1):
            total[i] += 1
        fail[stage] += 1
    fail_rate = [[i, 0] for i in range(max_stage)]

    for i in range(N+1):
        if total[i] != 0:
            fail_rate[i] = [i, fail[i] / total[i]]

    fail_rate = sorted(fail_rate[1:N+1], key=lambda x: x[1], reverse=True)

    return [stage for stage, rate in fail_rate]

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 실패율이 높은것 부터 내림차순.
# 실패율이 같다면 스테이지가 낮은 것 부터 출력
N = [5, 4, 100]
stages = [[2, 1,2,6,2,4,3,3], [4 ,4 ,4 ,4 ,4], [1, 2, 3, 3, 2, 5, 6, 7, 6, 5, 5,5 ,5 ,5 ,5 ,4 ,3 ,100]]
results = [[3, 4, 2, 1, 5], [4, 1,2,3], [0]]
for i in range(len(N)):
    my_answer = solution(N[i], stages[i])
    print(results[i])
    print(my_answer)
