import collections

def solution(n, a, b):
    answer = 1

    while True:
        a = a/2
        b = b/2

        if type(a) != int:
            a = (int)(a+0.5)
        if type(b) != int:
            b = (int)(b+0.5)

        if a == b:
            break
        answer += 1

    #print(answer)
    return answer


if __name__ == "__main__":
    #n, a, b = map(int, input().split())
    n ,a, b = 8,4,7
    solution(n,a,b)