string = input()
N = len(string)
# R <= C and R*C = N
R, C = 0, 0
for i in range(1, N//2):
    if N%i == 0:
        if N//i >= i:
            R = max(R, i)
C = N//R
for i in range(R):
    for j in range(C):
        print(string[i+R*j], end='')