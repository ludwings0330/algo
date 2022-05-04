def solution(cookie):
    answer = 0
    LEN = len(cookie)
    cs = 0
    ce = LEN
    for i in range(LEN):
        s = cs + i
        e = ce - i
        for m in range(s, e):
            sumLeft = 0

            for l in range(m, s-1, -1):
                sumLeft += cookie[l]
                sumRight = 0

                for r in range(m+1, e):
                    sumRight += cookie[r]

                    if sumLeft == sumRight:
                        answer = max(answer, sumLeft)
                    elif sumLeft < sumRight:
                        break
        if answer != 0:
            return answer
    return answer

cookie = [[1,1,2,3], [1,2,4,5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for c in cookie:
    print(solution(c))