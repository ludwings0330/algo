N = int(input())

MAX = 0
MIN = float('inf')

# 문제를 잘못 읽어서 못풀었던 문제...

def recursiveSolve(N,d):
    if N < 10:
        global MAX, MIN
        if N % 2 == 0:
            MAX = max(MAX, d)
            MIN = min(MIN, d)
            return 0
        else:
            MAX = max(MAX, d+1)
            MIN = min(MIN, d+1)
            return 1
    elif N < 100:
        a, b = N // 10, N % 10
        ret = 0
        if a % 2 == 1:  # 홀수라면
            ret += 1
        if b % 2 == 1:
            ret += 1
        ret + recursiveSolve(a + b, d + ret)
    else:
        # N 이 3자리 이상
        k1 = 1
        tmpN = N
        ret = 0
        while tmpN!=0:
            if tmpN %2 == 1:
                ret += 1
            tmpN //= 10

        while N // (10 ** k1) >= 10:
            k2 = k1 + 1
            while N // (10 ** k2) > 0:
                a = N // (10 ** k2)
                b = N % (10 ** k2) // (10 ** k1)
                c = N % (10 ** k1)
                k2 += 1
                recursiveSolve(a + b + c, d+ret)

            k1 += 1
            # print("answer : {}".format(ret))

    return 0


recursiveSolve(N,0)
print(MIN, MAX)
