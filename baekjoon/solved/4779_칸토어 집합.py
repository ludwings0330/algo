
def recursiveSolve(cantor):
    if len(cantor) == 1:
        return '-'
    if len(cantor) == 3:
        cantor = '- -'
        return cantor # 잘마무리 되었음 1

    interval = int(len(cantor) / 3)
    answer = ""

    answer += recursiveSolve(cantor[:interval])
    answer += " "*interval
    answer += recursiveSolve(cantor[interval*2:])

    return answer

while True:
    try:
        N = int(input())
        cantor = '-'*(3**N)
        print(recursiveSolve(cantor))

    except EOFError:
        break