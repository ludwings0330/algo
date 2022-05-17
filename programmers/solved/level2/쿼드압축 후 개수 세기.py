def recursive_solve(arr, sr, sc, er, ec):
    ret = ""
    char = arr[sr][sc]
    isOk = True

    for r in range(sr, er):
        for c in range(sc, ec):
            if arr[r][c] != char:
                # 다르면 4 개로 나눠야함
                isOk = False
                mr = (sr + er) // 2
                mc = (sc + ec) // 2

                ret += recursive_solve(arr, sr, sc, mr, mc)
                ret += recursive_solve(arr, sr, mc, mr, ec)
                ret += recursive_solve(arr, mr, sc, er, mc)
                ret += recursive_solve(arr, mr, mc, er, ec)

                break
        if not isOk:
            break

    if isOk:
        ret = str(char)

    return ret


def solution(arr):
    s = recursive_solve(arr, 0, 0, len(arr), len(arr[0]))

    return [s.count("0"), s.count("1")]


arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))
