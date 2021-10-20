import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**9)

skills = []

while True:
    try:
        w, b = map(int, input().split())
        skills.append([w, b])
    except:
        break

N = len(skills)

def select(n, white, black):
    # 팀을 전부다 뽑았으면 종료
    if white == 0 and black == 0:
        return 0
    if n == N or (white < 0 or black < 0):
        # 이 경우 답이 될 수 없음
        return -987654321

    if cache[n][white][black] != -1:
        return cache[n][white][black]

    cache[n][white][black] = max(select(n + 1,   white - 1, black) + skills[n][0],
                              select(n + 1,  white, black - 1) + skills[n][1],
                              select(n + 1,  white, black))

    return cache[n][white][black]

cache = [[[-1] * 16 for _ in range(16)] for _ in range(1002)]

print(select(0, 15, 15))

'''
백으로 15명, 흑으로 15명을 뽑아야한다. 가능한 최고의 팀을 만들려고할때, 

select(n, white, black) -> n명 중에 white 명, black 명 뽑아서 만들 수 있는 최대 점수 반환

1. n번 선수를 백팀으로 뽑느다.
2. n번 선수를 흑팀으로 뽑는다.
3. n번 선수를 뽑지않는다.  
'''