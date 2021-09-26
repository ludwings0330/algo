def check(x, y):
    pass



def solution(p, q):
    answer = []
    for i in range(len(p)):
        answer.append(check(p[i], q[i]))


    return answer




p = [[5,3,2,2,1]]
q = [[7,2,4]]
print(solution(p, q))

p = [[4,3,3],[1,2,3],[3,2,4]]
q = [[5,5],[5,1],[1,8]]
print(solution(p, q))