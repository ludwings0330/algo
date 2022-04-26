def solution(nums):
    # len : 3 ~ 50
    # 숫자 3개를 더해서 소수가 되는 경우의 수
    answer = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if prime[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer

prime = [True]* 3001
for i in range(2, 3001):
    if prime[i]:
        k = 2
        while i*k < 3001:
            prime[i*k] = False
            k += 1

nums = [[1, 2, 3, 4], [1, 2, 7, 6, 4]]
results = [1, 4]
for i, num in enumerate(nums):
    print(results[i])
    print(solution(num))