def solution(n):
    answer = ''
    patterns = ['0','1','2','4']

    while n>3:
        tmp = n%3
        n=n//3
        if tmp == 0:
            n-=1
            tmp=3
        answer += patterns[tmp]

    answer += patterns[n]
    answer = answer[::-1]
    print(answer)

    return answer

if __name__ == "__main__":
    n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #1,2,4,11
    for i in n:
        solution(i)
