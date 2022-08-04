# 일곱난장이 키의 합이 100

heights = [int(input()) for _ in range(9)]

def sum(total, to_pick: int, picked: list, start):
    if total > 100:
        return False

    if to_pick == 0:
        if total == 100:
            print(*sorted(picked), sep='\n')
            return True
        return False

    for next in range(start, len(heights)):
        if sum(total + heights[next], to_pick - 1, picked + [heights[next]], next+1):
            return True

    return False

sum(0, 7, [], 0)