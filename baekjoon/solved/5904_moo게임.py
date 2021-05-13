moolen = [3]
index = 0
while moolen[-1] <= 10**9:
    moolen.append(moolen[index]*2+(index+4))
    index+=1

# S(N)의 N번째 문자를 찾아라
def recursiveSolve(N, index):
    # N 번째 수를 찾고 있어요
    if index == -1:
        if N == 1:
            return 'm'
        else:
            return 'o'
    if moolen[index] > N: # 왼쪽
        return recursiveSolve(N, index-1)
    elif moolen[index] + index + 4 >= N: # 중앙
        if N-moolen[index] == 1:
            return 'm'
        else:
            return 'o'
    else: # 오른쪽
        return recursiveSolve(N - moolen[index] - index - 4, index)
# while True:
N=int(input())
print(recursiveSolve(N, len(moolen)-1))