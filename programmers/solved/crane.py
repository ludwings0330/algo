import collections

def solution(board, moves):
    answer = 0

    dq = []
    count = 0
    for i in moves: # i 열
        for depth in range(len(board[0])):
            if board[depth][i-1] != 0:
                dq.append(board[depth][i-1])
                board[depth][i-1] = 0
                break


    while True:
        length = len(dq[:-1])
        if length < 1:
            break

        flag = True

        for i in range(length):
            if dq[i] == dq[i+1]:
                answer += 2
                del dq[i+1], dq[i]
                flag = False
                break

        if flag:
            break


    return answer


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

    solution(board, moves)

