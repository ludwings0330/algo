def solution(m, n, board):
    answer = 0
    # 높이 m 폭 n 정보 board

    # for i in range(m):
    #     line = ''
    #     for j in range(n):
    #         line += board[i][j]
    #     print(line)
    board_list = list(map(list,board))
    print(board_list)

    data = []
    for i in range(m-1):
        line = ''
        for j in range(n-1):
            if board[i][j] == board[i+1][j+1] == board[i+1][j] == board[i][j+1]:
                data.append([i,j])

    for i,j in data:
        board_list[i][j] = board_list[i+1][j+1] = board_list[i+1][j] = board_list[i][j+1] = '0'


    return answer

if __name__ == "__main__":

    m = 6
    n = 6
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    print("answer is {}".format(solution(m,n,board)))
