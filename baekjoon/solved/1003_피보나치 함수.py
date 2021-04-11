import sys
def fibo(N):
    if N == 0:
        print('0')
        return 0
    elif N == 1:
        print('1')
        return 1
    else:
        return fibo(N-1) + fibo(N-2)


if __name__ == "__main__":
    T = int(input())
    dic = {0:[1,0], 1:[0,1]}
    index = 1
    for i in range(T):
        N = int(sys.stdin.readline().rstrip())
        if N > index:
            for j in range(index+1, N+1):
                dic[j] = [dic[j-2][0] + dic[j-1][0] , dic[j-2][1] + dic[j-1][1]]
        print(dic[N][0], dic[N][1])