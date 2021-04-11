
if __name__ == "__main__":
    N, M = map(int, input().split())
    card = list(map(int, input().split()))
    MAX = -1
    answer = []

    for i in range(len(card)-2):
        for j in range(i+1,len(card)-1):
            for k in range(j+1,len(card)):
                blackjack = card[i]+card[j]+card[k]
                if blackjack <= M:
                    answer.append(blackjack)

    print(max(answer))