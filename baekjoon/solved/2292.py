N = int(input())
i = 1
k = 1
while True:
    if i >= N:
        break
    else:
        i += k*6
        k+=1
print(k)