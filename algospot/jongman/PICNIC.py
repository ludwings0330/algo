if __name__ == "__main__":
    C = int(input())

    while C > 0:
        C -= 1

        n, m = map(int, input().split())

        answer = 0
        visit = [False] * n
        areFriends = [[0]*10 for i in range(10)]
        friendList = list(map(int, input().split()))
        # friendList[i] 하고 freindList[i+1] 은 서로 친구 짝이 될 수 있음.
        for i in range(0, len(friendList), 2):
            areFriends[friendList[i]][friendList[i+1]] = 1
            areFriends[friendList[i+1]][friendList[i]] = 1


        def recursionMatch(ivisit):
            firstFree = -1
            for i in range(n):
                if not ivisit[i]:
                    firstFree = i
                    break
            if firstFree == -1:
                return 1

            ret = 0

            for i in range(firstFree + 1, n):
                if not ivisit[i] and areFriends[firstFree][i]:
                    ivisit[i] = ivisit[firstFree] = True
                    ret = recursionMatch(ivisit)
                    ivisit[i] = ivisit[firstFree] = False

            return ret

        print(recursionMatch(visit))