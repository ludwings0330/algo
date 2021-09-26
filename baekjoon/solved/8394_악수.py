import sys
sys.setrecursionlimit(10**9)
def handShake(i): # 현재 사람 번호가 i 일 때 악수를 하는 방법의
    if i == n:
        return 1 # 모두 악수를 했으니 경우의 수를 1 더해준다
    if i > n:
        return 0
    if cache[i] != -1:
        return cache[i]

    cache[i] = 0
    # i 번째 사람이 오른쪽 사람과 악수를 한다

    cache[i] += handShake(i+2)
    cache[i] %= 10

    # i 번째 사람이 오른쪽 사람과 악수를 하지 않는다.
    cache[i] += handShake(i+1)
    cache[i] %= 10
    return cache[i]

n = int(input())

cache = [-1] *(n+1)
cache[1] = 1
cache[2] = 2

for i in range(3, n+1):
    cache[i] = (cache[i-2] + cache[i-1]) % 10
print(cache[n])