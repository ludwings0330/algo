import re
from collections import defaultdict
test_case = 1
while True:
    try:
        K, E = map(int, input().split())
        keyword = set()
        for _ in range(K):
            keyword.add(input().lower())

        ans_count = 0
        ans_excuse = [""]
        for e in range(E):
            origin_excuse = input()
            excuse = re.sub('[^a-z0-9]', ' ', origin_excuse.lower())
            excuse = excuse.split()
            store = defaultdict(int)
            for ex in excuse:
                store[ex] += 1
            count = 0
            for key in keyword:
                count += store[key]
            if ans_count < count:
                ans_count = count
                ans_excuse = [origin_excuse]
            elif ans_count == count:
                ans_excuse.append(origin_excuse)

        print(f'Excuse Set #{test_case}')
        test_case += 1
        print(*ans_excuse, sep="\n")
        print()
    except EOFError:
        break