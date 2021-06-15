N = int(input())
score = list(map(int, input().split()))
MAX = max(score)
for i in range(len(score)):
    score[i] = score[i]/MAX*100
print(sum(score)/len(score))