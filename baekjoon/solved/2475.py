if __name__ == "__main__":
    li = list(map(int, input().split()))
    tmp = 0
    for i in range(len(li)):
        tmp += li[i]**2
    print(tmp%10)