C = int(input())

def match(w, s):
    if cache[w][s] != -1:
        return cache[w][s]

    while w < len(wildCard) and s < len(ss) and (wildCard[w] == ss[s] or wildCard[w] == '?'):
        w += 1
        s += 1


    if w == len(wildCard):
        if s == len(ss):
            cache[w][s] = True
            return cache[w][s]
        else:
            cache[w][s] = False
            return cache[w][s]

    if wildCard[w] == '*':
        # 여기 까지 왔으면 wildCard[w] == '*' 이라는 뜻이다. 그럼 몇글자를.... 건너 뛸지 고민해 봐야지. 모든 경우의 수를 따져야하니까
        # s+skip 에서 skip 은 0 ~ s가 마지막이 될 때 까지다.
        ret = False
        for skip in range(1, len(ss) - s + 1):
           if match(w+1, s + skip):
               cache[w][s] = True
               return cache[w][s]

        cache[w][s] = False
        return cache[w][s]


for testCase in range(1, C+1):
    wildCard = input()

    N = int(input())
    userInput = [input() for _ in range(N)]

    ans = []

    for ss in userInput:
        cache = [[-1] * (len(ss)+1) for _ in range(len(wildCard)+1)]
        if match(0, 0):
            ans.append(ss)

    print(ans)