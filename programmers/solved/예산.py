# 최대한 많은 부서의 물품을 구매
# 1000원을 신청한 부서에는 정확히 1000을 지, 1000원보다 적은 금액을 지원할 수 없음
# 최대 몇개의 부서에 물품을 지원할 수 있는지 return 하는 함수 작성


def solution(d, budget):
    answer = 0
    d.sort()
    index = 0
    while index < len(d):
        if budget - d[index] < 0:
            break
        else:
            budget -= d[index]
            index += 1
            answer += 1
    return answer


dd = [[1,3,2,5,4], [2,2,2,3]]
budgets = [9, 10]
results = [3, 4]

for i in range(len(dd)):
    result = solution(dd[i], budgets[i])

    print("expected : ", results[i])
    print("my answer : ", result)