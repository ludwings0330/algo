def solution(n):
    answer = []

    c = 1
    d = 0
    tag = -1

    answer = [[0 for j in range(n)] for i in range(n)]

    row, row_p = 0, 1
    col, col_p = 0, 1

    for i in range(n):
        for j in range(n):
            answer[row][col] = c
            c += 1
            row += row_p
            col += col_p

            if row == n-d and col == n-d:
                row_p *= tag
                col_p *= tag
                d += 1



    return answer



if __name__ == "__main__":
    n = 4
    print(solution(n))
