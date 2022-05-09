from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0
    dq = deque()
    for city in cities:
        city = city.lower()

        if city in dq:
            answer += 1
            dq.remove(city)
            dq.appendleft(city)
        else:
            if len(dq) == cacheSize:
                dq.pop()
            answer += 5
            dq.appendleft(city)

    return answer

# 0 <= cacheSize <= 30
# 1 <= len(cities) <= 100,000
# cities 는 영문자로 구성, 대소문자 구분 X, 최대 20 글자
# 입력된 도시이름 배열을 순서대로 처리할 때 "총 실행시간"을 출력한다.
# 캐시 크기에 따른 실행시간 출력

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cacheSize = 3

print(solution(cacheSize, cities))
