def solution(a,b):
    answer = 0
    if a>b:
        a, b = b, a

    for i in range(a,b+1):
        answer += i

    return answer


if __name__ == "__main__":
    solution(3,5)