if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        H, W, N = map(int, input().split())
        n = (N//H)
        if N%H !=0:
            n += 1
        f = N%H # 층수정보
        if f == 0:
            f = H
        n = format(n,'02')
        print("{}{}".format(f,n))