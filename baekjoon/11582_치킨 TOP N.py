import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
score = list(map(int, input().split()))
k = int(input())

def merge_sort(people, scores):
    if len(scores) == 1:
        return scores

    mid = len(scores) // 2

    left = merge_sort(people*2, scores[:mid])
    right = merge_sort(people*2, scores[mid:])

    if people < k:
        return left + right

    ret = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1

    return ret + left[l:] + right[r:]

print(*merge_sort(1, score))
