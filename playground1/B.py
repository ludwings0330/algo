import sys
input = sys.stdin.readline

T = int(input())
visit = set()
def solve(left, right, toPick, i, k):
    if toPick == 0 or k == 0:
        right += cards[i:]
        if left and right:
            left = int(''.join(str(c) for c in left))
            right = int(''.join(str(c) for c in right))
            global ans
            ans = max(ans, left*right)
        return
    if len(left) == len(right):
        solve(left + [cards[i]], right, toPick-1, i+1, k-1)
    else:
        solve(left, right + [cards[i]], toPick-1, i+1, k)

while T:
    T -= 1
    cards = list(map(int, list(input().rstrip())))
    for i, c in enumerate(cards):
        if c == 6:
            cards[i] = 9

    cards.sort(reverse = True)
    ans = 0
    for k in range(len(cards)):
        solve([], [], len(cards), 0, k)
    print(ans)