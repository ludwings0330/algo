strA = list(input())
strB = list(input())

cache = [[0] * len(strA) for _ in range(len(strB))]
# cache[strB][strA]

ANS = 0
for i in range(len(strA)):
    for j in range(len(strB)):
        if strA[i] == strB[j]:
            if i == 0 or j == 0:
                cache[j][i] = 1
            else:
                cache[j][i] = cache[j-1][i-1] + 1
                ANS = max(ANS, cache[j][i])

print(ANS)