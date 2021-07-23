import sys
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    n, k = map(int, input().split())
    x = input().rstrip().split()
    # n개의 자동차, 길이가 k인 번호판 문자열

    # 각 알파뱃 해당 알파벳이 x[i]에 적힌 횟수와 x[j]에 적힌 횟수가 같다.
    # x[i]에 적힌 대문자의 개수와 x[j]에 적힌 대문자의 개수가 같다.
    board = {}
    for ss in x:
        numOfUpper = sum(c.isupper() for c in ss)
        ss = ss.lower()
        key = tuple(sorted(list(ss)))
        if key not in board:
            board[key] = {numOfUpper:1}
        elif key in board:
            if numOfUpper in board[key]:
                board[key][numOfUpper] += 1
            else:
                board[key][numOfUpper] = 1
    ret = 0
    for key in board:
        for upper in board[key]:
            n = board[key][upper]
            ret += n*(n-1)//2

    print(ret)