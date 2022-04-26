# 최대한 많은 수의 폰켓몬 고르기 최대 N//2
def solution(nums):
    return len(set(nums)) if len(set(nums)) <= len(nums)//2 else len(nums)//2

nums = [[3,1,2,3], [3,3,3,2,2,4], [3,3,3, 2,2,2,]]
results = [2, 3, 2]

for i, num in enumerate(nums):
    print(results[i])
    print(solution(num))