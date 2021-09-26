# 백준 마라톤 대회
# N 교차로
# M 도로
# K 예산

N, M, K = map(int, input().split())
graph = {}

for _ in range(M):
    A, B, C, T = map(int, input().split())
    # P > T 인경우 통제 비용 = C*(P-T)**2
    if A in graph:
        graph[A][B] = (C, T)
    else:
        graph[A] = {B:(C, T)}
    if B in graph:
        graph[B][A] = (C, T)
    else:
        graph[B] = {A:(C, T)}

# 예산안에서 경로를 적절히 선택하고 마라톤 최대 인원 P를 출력해라
# 시작은 항상 1 에서 종료는 N -> 다익스트라
# 1. 모든 정점을 방문해야 한다
# 2. 모든 정점을 방문하면서도 최대한 싸게 방문
# 