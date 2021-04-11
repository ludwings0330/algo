#프로그래머스 더맵게.py
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
#
# scoville의 길이는 2 이상 1,000,000 이하입니다.
# K는 0 이상 1,000,000,000 이하입니다.
# scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)
    count = 0
    while True:
        n = heapq.heappop(h)
        if n >= K:
            break
        try:
            n = n+heapq.heappop(h)*2
            heapq.heappush(h, n)
            count += 1
        except:
            return -1
    answer = count

    return answer

if __name__ == "__main__":
    scoville = [1,2,3,9,10,12]
    K = 7
    # answer = 2

    print("K is {}".format(solution(scoville, K)))