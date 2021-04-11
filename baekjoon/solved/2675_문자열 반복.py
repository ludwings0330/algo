if __name__=="__main__":
    N = int(input())

    for i in range(N):
        command = input().split()
        num = int(command[0])
        strList = list(command[1])
        for ch in strList:
            print(ch*num,end='')
        print()
