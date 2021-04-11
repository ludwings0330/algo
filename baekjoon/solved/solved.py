if __name__=="__main__":
    N = int(input())

    for i in range(N):
        quizList = list(input())
        count = 1
        score = 0
        for a in quizList:
            if a == 'O':
                score += count
                count +=1
            else:#X
                count = 1
        print(score)
