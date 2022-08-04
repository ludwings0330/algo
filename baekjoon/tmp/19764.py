from collections import defaultdict

n = int(input())
candidates = []

month_count = defaultdict(int)
day_count = defaultdict(int)

for _ in range(n):
    d, m = map(int, input().split())
    candidates.append((d, m))

    # m월이 month_count[m] 개 있다.
    month_count[m] += 1
    # d일이 day_count[d] 개 있다.
    day_count[d] += 1

summarized_candidates = []
t_month_count = defaultdict(int)
t_day_count = defaultdict(int)

for d, m in candidates:
    # 일자가 1개인거 제외, 달이 1개인거 제외
    if month_count[m] > 1 and day_count[d] > 1:
        summarized_candidates.append((d, m))
        # 일자가 1개인거와 달이 1개인거 제외하고 다시 센다.
        t_month_count[m] += 1
        t_day_count[d] += 1

candidates = []
month_count = defaultdict(int)
day_count = defaultdict(int)
for d, m in summarized_candidates:
    # 달이 1개인게 다시 정답 후보가 된다.
    if t_day_count[d] == 1:
        candidates.append((d, m))
        month_count[m] += 1
        day_count[d] += 1

for d, m in candidates:
    if month_count[m] == 1 and day_count[d] == 1:
        print(d, m)