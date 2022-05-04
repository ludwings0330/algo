def solution(n):
    answer = True
    return True if n % sum(list(map(int, list(str(n))))) == 0 else False