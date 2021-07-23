import sys
def solution(lottery):
    answer = 0
    win = [False]*1001
    purchase = [0]*1001

    winDict = {}

    for id, f in lottery:
        if not win[id]: # 아직 당첨이 아니면
            purchase[id] += 1

            if f == 1: #당첨 됐으면
                win[id] = True # 당첨.
                winDict[id] = purchase[id] # 당첨된 목록에 횟수를 추가
    SUM = 0
    for id in winDict:
        SUM += winDict[id]
    if len(winDict) != 0:
        answer = SUM//len(winDict)
    return answer

l = [[1,0],[35,0],[1,0],[100,1],[35,1],[100,1],[35,0],[1,1],[1,1]]
l2 = [[1,0],[2,0],[3,0],[1,0],[2,0],[1,0],[1,1],[2,0],[2,0],[2,1],[1,0],[1,1],[3,0],[3,0],[1,1]]
l3 = [[1,0],[2,0],[3,0]]
print(solution(l))
print(solution(l2))
print(solution(l3))
