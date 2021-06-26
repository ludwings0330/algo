import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
ss = []
for i in range(N):
    ss.append(int(input()))

# 단순하게 풀기
# !!! 시간초과 !!! #
# ------- 단순하게 풀기 ------- #

# answer = 0
# for i in range(N):
#     st = []
#     count = 0
#     flag = True
#     for j in range(k):
#         s = ss[(i+j)%N]
#         if s not in st:
#             st.append(s)
#             count += 1
#             if s == c:
#                 flag = False
#     if flag:
#         count += 1
#     answer = max(answer, count)
# print(answer)

# !!!시간 초과!!! #
# ------- eof 단순하게 풀기 --- #

# ------ 시간 줄이기 ----- #
visit = [0] * (d+1)
MAX = 0
count = 0
for i in range(k):
    if not visit[ss[i]]:
        count += 1
    visit[ss[i]] += 1

s = 0
e = k-1
for i in range(N):
    if MAX <= count:
        if not visit[c]:
            MAX = count + 1
        else:
            MAX = count

    visit[ss[s]] -= 1
    if not visit[ss[s]]:
        count -= 1
    if not visit[ss[(e + 1) % N]]:
        count += 1
    visit[ss[(e + 1) % N]] += 1

    s += 1
    e += 1

print(MAX)