'''
마법 천자문

+, - 로 이루어진 문자열,
+ 는 10 혹은 +
- 는 1 혹은 -

최대로 만들어보자.
수로시작해서, 수로 끝난다.

수는 +-, +, - 중 하나, 11, 10, 1
연산자는 +, - 중 하나, 더하기 빼기로 해석


-> 다이나믹 프로그래밍 풀이

solve(cur) -> 현재 위치가 cur 일때, 조합을 통해 만들수 있는 최대 값.

'''

def solve(cur, t):



    if cache[cur][t] != -1:
        return cache[cur][t]

    if A[cur] == '+':


    return cache[cur][t]
while True:
    A = list(input())
    N = len(A)

    cache = [[-1]* 2 for _ in range(N + 1)]

    print(solve(0, 1))
    print()
