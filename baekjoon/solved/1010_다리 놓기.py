T = int(input())
while T:
    T -= 1
    N, M = map(int, input().split())
    answer = M

    #순서에 상관없이 M개 중 N개를 선택하는 경우의 수
    #mCn
    #m*(m-1)*(m-2)*(m-3) ..... / n!
    for i in range(1, N):
        answer = int( answer * (M-i) / (i+1) )

    print(answer)