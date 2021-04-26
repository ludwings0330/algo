N = int(input())
count = -1
for i in range(N//3+1):
    if count != -1:
        break
    for j in range(N//5+1):
        if 3*i + 5*j == N:
            count = i+j
            break
print(count)