str1 = [' ']
str1.extend(list(input()))
str2 = [' ']
str2.extend(list(input()))
LCS = [[0]*(len(str1)) for _ in range(len(str2))]

for i in range(len(str1)):
    for j in range(len(str2)):
        if i == 0 or j == 0 :
            LCS[j][i] = 0
        elif str1[i] == str2[j]:
            LCS[j][i] = LCS[j-1][i-1] + 1
        else:
            LCS[j][i] = max(LCS[j-1][i], LCS[j][i-1])
print(max(LCS[-1]))