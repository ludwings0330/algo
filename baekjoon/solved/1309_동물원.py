N = int(input())
DIV = 9901

'''
가로로도, 세로로도 붙어있게 배치할 수는 없다.
사자를 배치하는 경우의 수는 몇 가지 인가
'''

cache = [-1] * N

def solve(r):
    if r >= N:
        return 1


    if cache[r] != -1:
        return cache[r]

    cache[r] = 0
    cache[r] = (solve(r+1) + solve(r+2))%DIV

    return cache[r]

print(solve(0))