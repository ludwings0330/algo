N = int(input())

def recursiveSolve(n):
    if n == 1:
        return print(1, end = '')
    elif n == 0:
        return print(0, end = '')

    recursiveSolve(n//2)
    print(n%2, end = '')

recursiveSolve(N)