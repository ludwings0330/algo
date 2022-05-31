def solution(N, number):
    if N == number:
        return 1

    answer = 0
    dp = [set()] + [set([int(str(N)*i)]) for i in range(1, 9)]

    for i in range(2, 9):
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].add(k+l)
                    if k-l > 0:
                        dp[i].add(k-l)
                    dp[i].add(k*l)
                    if l != 0 and k != 0:
                        dp[i].add(k//l)
            if number in dp[i]:
                return i

    return -1


print(solution(5, 12))
print(solution(2, 11))