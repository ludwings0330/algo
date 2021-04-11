import sys

if __name__ == "__main__":
    N, M = map(int, input().split())
    names = set()
    answer = set()
    for i in range(N):
        name = sys.stdin.readline().rstrip()
        names.add(name)

    for i in range(M):
        name = sys.stdin.readline().rstrip()
        if name in names:
            answer.add(name)

    print(len(answer))
    answerList = list(answer)
    answerList.sort()
    for i in answerList:
        print(i)
        