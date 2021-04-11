if __name__ == "__main__":
    input()
    li = list(map(int, list(input())))
    tmp = 0
    for i in range(len(li)):
        tmp += li[i]
    print(tmp)