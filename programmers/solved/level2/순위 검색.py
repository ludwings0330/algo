# [조건]을 만족하는 사람 중 코팅 테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
# 1<= info <= 50,000
# 1 <= query <= 100,000
from collections import defaultdict
import itertools


def solution(infos, queries):
    info_dict = defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))

    for inf in infos:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)])
            info_dict[key].append(int(inf[4]))

    for k in info_dict.keys():
        info_dict[k].sort()

    answer = []

    for query in queries:
        q = [q for q in query.split() if q != 'and']

        key = ''.join(q[:-1])
        target = int(q[-1])

        arr = info_dict[key]
        mid = left = 0
        right = len(arr)
        if right == 0:
            answer.append(0)
            continue

        c = 0
        while left < right:
            mid = (left + right) // 2
            if target > arr[mid]:
                left = mid + 1
            else:
                right = mid
        answer.append(len(info_dict[key]) - right)

    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150",
         "cpp and frontend and - and - 150"]

print(solution(info, query))