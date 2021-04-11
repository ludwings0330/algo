def solution(n, t, m, p):
    answer = ''
    num = list("0123456789ABCDEF")
    count = 0
    number = 0
    rot = 0

    while t > 0:
        tmp = number
        line = []
        if tmp == 0:
            line = ['0']

        while tmp > 0:
            line.append(num[tmp%n])
            tmp //= n
        count += len(line)
        if count >= p:
            answer += line[(count-p)]
            p += m
            t -= 1
        number += 1
    #15B16C3B4E9520FF
    #15B1112233456778
    return answer

if __name__ == "__main__":
    n,t,m,p = 16,16,2,1
    print("answer is {}".format(solution(n,t,m,p)))