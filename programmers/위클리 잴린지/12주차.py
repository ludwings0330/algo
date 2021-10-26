'''
현재 피로도 k
최소 필요 피로도, 소모 피로도 dungeons

유저가 탐험할 수 있는 최대 던전 수
던전 방문 순서가 중요하다.

던전 개수가 8이기 때문에 완전탐색 가능 8!
'''

visit = [False]*8
n = 0
g_dungeons = []
def explore(k):
    ret = 0
    for i in range(n):
        if visit[i]:
            continue
        else:
            if g_dungeons[i][0] <= k:
                visit[i] = True
                ret = max(ret, explore(k-g_dungeons[i][1]) + 1)
                visit[i] = False
            else:
                continue

    return ret


def solution(k, dungeons):
    global n, g_dungeons
    n= len(dungeons)
    g_dungeons=dungeons

    answer = explore(k)
    return answer

k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
