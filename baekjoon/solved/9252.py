# LCS 2
# 최대 1000 글자. 1. LCS 길이, 둘쨰 줄에 LCS 출력

import sys
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
LCS = [[0] * (len(str1) + 1) for _ in range(len(str2) +1)]

for i in range(len(str2)+1):
    for j in range(len(str1)+1):
        if i == 0 or j == 0:
            LCS[i][j] = 0
            continue

        if str2[i-1] == str1[j-1]: #같다면
            LCS[i][j] = LCS[i-1][j-1] + 1
        else: # 다르다면
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
MAX = LCS[-1][-1]
print(MAX)
i = len(str2)
j = len(str1)
answer = []
while LCS[i][j]:
    if LCS[i][j] == LCS[i-1][j]:
        i -= 1
    elif LCS[i][j] == LCS[i][j-1]:
        j -= 1
    else:
        answer.append(str1[j-1])
        j-=1
        i-=1

print(''.join(answer[::-1]))