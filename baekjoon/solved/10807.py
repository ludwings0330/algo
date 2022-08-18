from collections import Counter
input()
counter = Counter(list(map(int,input().split())))
print(counter[int(input())])