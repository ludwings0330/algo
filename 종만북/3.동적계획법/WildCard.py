import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(w: int, s: int):
    if cache[w][s] != -1:
        return cache[w][s]
    while w < len(wild_card) and s < len(ss) and (wild_card[w] == '?' or wild_card[w] == ss[s]):
        w += 1
        s += 1
    # wild card 끝에 도달한 경우
    if w == len(wild_card):
        # 문자열도 끝에 도달 했어야 한다.
        cache[w][s] = (s == len(ss))
        return cache[w][s]

    if wild_card[w] == '*':
        # 다음 글자를 포함하거나 포함하지 않도록 처리
        if (solve(w + 1, s)) or (s < len(ss) and solve(w, s + 1)):
            cache[w][s] = 1
            return cache[w][s]

    # 그외의 경우에는 모두 답이 아니다.
    cache[w][s] = 0
    return cache[w][s]


t = int(input())
while t:
    t -= 1

    wild_card = input()
    n = int(input())

    user_input = [input() for _ in range(n)]
    ans = []
    for ss in user_input:
        cache = [[-1] * 101 for _ in range(101)]

        if solve(0, 0):
            ans.append(ss)
    ans.sort()
    print(*ans, sep='\n')
