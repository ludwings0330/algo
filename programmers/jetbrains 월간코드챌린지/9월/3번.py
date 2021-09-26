def solution(a, b, g, s, w, t):
    answer = -1
    cities = list(zip(g, s, w, t))
    cities.sort(key = lambda x:min(x[2], x[0]+x[1])/x[3], reverse= True)
    cities = [list(city) for city in cities]
    N = len(g)
    numOfRepeat = [0] * N

    GOLD, SILVER, WEIGHT, TIME = [0, 1, 2, 3]

    for i in range(N):
        while cities[i][0] > 0 and a > 0:
            a -= min(cities[i][WEIGHT], cities[i][GOLD])
            cities[i][GOLD] -= cities[i][WEIGHT]
            numOfRepeat[i] += 2

        if cities[i][GOLD] < 0: # 마지막에 가져다줄때 빈자리가 있었어 그만큼을 실버를 가져가자
            b -= min(cities[i][SILVER], abs(cities[i][GOLD])) # 실버가져갔어. 남는실버,
            cities[i][SILVER] += cities[i][GOLD]
            a -= cities[i][GOLD]

        if a < 0:
            b -= min(abs(a), cities[i][SILVER])
            cities[i][SILVER] += a
            a = 0

        while cities[i][SILVER] > 0 and b > 0:
            b -= min(cities[i][WEIGHT], cities[i][SILVER])
            cities[i][SILVER] -= cities[i][WEIGHT]
            numOfRepeat[i] += 2

        if a <= 0 and b <= 0:
            break
    for i in range(N):
        numOfRepeat[i] = (numOfRepeat[i]-1)*cities[i][TIME]
    return max(numOfRepeat)

print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0,0, 500], [100, 100, 2], [4, 8, 1]))
