# 시작하기 위한 요구체력 - 시작전 가직 ㅗ있음
# 던전 끝났을때 소모되는 사용 체력

# 하루에 한번씩 탐험 - 던전 여러개 - 최대한 많이 탐색

# k : 현재 체력
# dungeonds : ["요구체력","사용체력"]
size = 0
answer = 0
visited = [False] * 8
path = [0] * 8
hp = 0
origin_dungeons = []
def check():
    tmp_k = hp
    cnt = 0
    for i in range(size):
        # 요구 체력보다 현재 체력이 높으면 방문가능
        if origin_dungeons[path[i]][0] <= tmp_k:
            # 갯수를 센다
            cnt += 1
            # 방문하면 체력을 사용
            tmp_k -= origin_dungeons[path[i]][1]
    return cnt


def perm(cnt):
    if size == cnt:
        global answer
        answer = max(answer, check())
    for i in range(size):
        if visited[i]:
            continue
        visited[i] = True
        path[cnt] = i
        perm(cnt + 1)
        visited[i] = False

def solution(k, dungeons):
    global answer, size, hp, origin_dungeons
    hp = k
    origin_dungeons = dungeons
    size = len(dungeons)

    perm(0)

    return answer

print(solution(80, [[80,20],[50,40], [30, 10]]))