from collections import defaultdict

board = [list("ABCDE"), list("BBBCC"), list("CCCBB"), list("CCCBB"), list("BBBCC")]
store = defaultdict(int)

for r in range(5):
    for c in range(5):
        if c + 3 <= 5:
            store[''.join(board[r][c:c+3])] += 1
        if r + 3 <= 5:
            store[board[r][c]+board[r+1][c]+board[r+2][c]] += 1
        if r < 3 and c < 3:
            store[''.join([board[r][c], board[r+1][c+1], board[r+2][c+2]])] += 1

N = int(input())
for _ in range(N):
    s = input()
    print(s, store[s])
