def check(a):
    #a[0] & a[1] & .... & a[n-1] == 0
    bit_list = [0] * 31
    #bit_list[i] 는 2^i 위치 켜진 비트 갯수

    for num in a:
        tnum = num
        i = 0
        while tnum:
            if tnum % 2 == 1:
                bit_list[i] += 1
            tnum //= 2
            i+=1
    ret = 0
    for i in range(len(bit_list)):
        if bit_list[i] == len(a):
           ret += 2**i
    return ret
    pass

def solution(m, b):
    answer = []
    idx = 0
    for i in m:
        a = b[idx: idx + i]
        idx += i

        answer.append(check(a))

    return answer
print(solution([2, 2,4], [3, 2,1,2,1,2,4,7]))