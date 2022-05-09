# 유일성 만족, 최소성 만족
def solution(relation):
    answer = []

    R = len(relation)
    C = len(relation[0])

    from collections import deque
    dq = deque([[i] for i in range(C)])

    while dq:
        candidates = dq.popleft()
        store = set()

        for r in range(R):
            store.add(''.join(relation[r][c] for c in candidates))

        # 유일성 검사
        if len(store) == R:
            isMin = True
            for ss in answer:
                if set(ss) == set(ss).intersection(candidates):
                    isMin = False
                    break
            # 최소성 검사
            if isMin:
                answer.append(candidates)

        for i in range(candidates[-1] + 1, C):
            dq.append(candidates + [i])


    return len(answer)


relations = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relations))
