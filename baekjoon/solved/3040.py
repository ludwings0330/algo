hatNum = []
for _ in range(9):
    hatNum.append(int(input()))

visit = [False]*9
answer = []
def Solve(i, SUM):
    if i == 8:
        return False
    if SUM == 100 and i == 7:
        return True
    for j in range(9):
        if not visit[j]:
            visit[j] = True
            if Solve(i+1, SUM + hatNum[j]):
                answer.append(hatNum[j])
                return True
            visit[j] = False
    return False

Solve(0, 0)
answer.reverse()
for n in answer:
    print(n)