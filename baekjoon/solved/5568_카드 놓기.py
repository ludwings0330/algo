n = int(input())
k = int(input())
cardList = []
answer = {}
visit = [False] * n
for i in range(n):
    cardList.append(int(input()))

def recursiveSolve(index, cards, toPick):
    if toPick == 0:
        answer[''.join(map(str, cards))] = 1
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            cards.append(cardList[i])

            recursiveSolve(i, cards, toPick - 1)

            cards.pop()
            visit[i] = False

recursiveSolve(0, [], k)
print(len(answer))
