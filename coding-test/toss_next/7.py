# 주식들을 구매해서 얻을 수 있는 최대 가치
# 각각의 주식은 최대 한개만 구매할 수 있다.
# 현재 가격과 가치가 있다. 낮은 가격, 높은 가치를 구매해야지

# 현재 money 가 있을때 얻을 수 있는 최대 가치

# 두가지 경우지
# 1. 현재 stock을 구매한다
# 2. 구매하지 않는다.
def recursive_solve(m, n):
    if n == size:
        return 0

    if cache[m][n] != -1:
        return cache[m][n]

    cache[m][n] = 0
    # 현재 주식을 사지 않는 경우
    cache[m][n] = max(cache[m][n], recursive_solve(m, n+1))
    # 현재 주식을 사는 경우
    # 현재 가격이 내가 가진 돈보다 같거나 작아야함
    if g_stocks[n][1] <= m:
        cache[m][n] = max(cache[m][n], recursive_solve(m - g_stocks[n][1], n+1) + g_stocks[n][0])

    return cache[m][n]


g_stocks = []
cache = []
size = 0
# stocks = ["가치", "가격"]
def solution(money, stocks):
    answer = 0
    global g_stocks, size, cache
    g_stocks = stocks
    size = len(stocks)
    cache = [[-1] * size for _ in range(money+1)]

    answer = recursive_solve(money, 0)

    return answer

print(solution(10, [[1,1],[3,5],[3,5],[4,9]]))