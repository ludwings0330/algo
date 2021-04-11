from collections import deque
import copy
if __name__ == "__main__":
    K = int(input())
    W, H = map(int, input().split())
    guid = []
    for i in range(H):
        guid.append(list(map(int, input().split())))
    # 0 은 평지 1 은 장애물.

    # 0,0 에서 W,H 까지
    print(guid)
    def BFS(x, y, k):
        dq = deque()
        tmp_guid = copy.deepcopy(guid)

        dq.append([x, y, k])
        