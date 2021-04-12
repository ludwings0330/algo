def recursiveSolve(x, cnt):
    if len(x)<2:
        if int(x)%3 == 0:
            return [cnt, 1]
        else:
            return [cnt, -1]

    y = 0

    for k in x:
        y += int(k)

    return recursiveSolve(str(y), cnt+1)

if __name__ == "__main__":
    x = input()
    answer = recursiveSolve(x, 0)
    print(answer[0])

    if answer[1] == -1:
        print('NO')
    else:
        print('YES')
