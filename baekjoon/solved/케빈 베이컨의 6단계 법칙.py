from collections import deque
import copy
# N 유저수 , M 친구 관계 수
if __name__ == "__main__":
    N, M = map(int, input().split())
    rel = dict()
    visit = [0] * (N+1)

    for i in range(M):
        f, t = map(int, input().split())
        if not rel.get(f): # 존재하지 않으면
            rel[f] = [t]
        else:
            rel[f].append(t)
        if not rel.get(t):
            rel[t] = [f]
        else: # 존재하면
            rel[t].append(f)

    def BFS(start, end):
        dq = deque()
        dq.append([rel[start], 1])
        visit_tmp = copy.deepcopy(visit)
        visit_tmp[start] = 1
        if start == end:
            return 0
        while dq:
            info = dq.popleft()
            node = info[0]
            lv = info[1]
            for i in node:
                if visit_tmp[i] == 0: # 거길 방문하지 않았다면.
                    visit_tmp[i] = 1
                    if i == end:
                        return lv
                        dq.clear()
                    else:
                        dq.append([rel[i], lv+1])
    min = -1
    people = -1
    for s in range(1, N+1):
        tmp = 0
        for e in range(1, N+1):
            tmp += BFS(s, e)
        if tmp < min or min == -1:
            people = s
            min = tmp

    print(people)