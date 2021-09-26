# TC = int(input())

def classify(s, e):
    # [s:e] 구간의 난이도를 반환한다.
    isSame = True
    for i in range(s, e-1):
        if nums[i] != nums[i+1]:
            isSame = False
            break
    if isSame:
        return 1 # 모두 같으면 1

    progressive = True
    for i in range(s, e-1):
        if nums[i+1] - nums[i] != nums[1] - nums[0]:
            progressive = False
            break
    if progressive and abs(nums[1] - nums[0]) == 1:
        return 2 # 공차수열 , 단조 증가 혹은 단조 감소 일때,

    alterating = True
    for i in range(s, e):
        if nums[i] != nums[s + i%2]:
            alterating = False
            break
    if alterating:
        return 4
    if progressive:
        return 5
    return 10



def memorize(begin):
    if begin == len(nums):
        return 0
    if cache[begin] != -1:
        return cache[begin]

    cache[begin] = float('inf')

    for L in range(3, 6):
        if begin + L <= len(nums):
            cache[begin] = min(cache[begin], memorize(begin + L) + classify(begin, begin + L))
    return cache[begin]

# 모든 숫자가 같을때 1
# 숫자가 1씩 단조증가 혹은 단조 감소 2
# 두개의 숫자가 번갈아다며 등장 4
# 숫자가 등차 수열을 이룰 때 5
# 이 외의 모든 경우 10

# memorize(begin) = min l=3->5 (memorize(begin + L)+classify(N))

TC = 5
numsList = ['12341234', '11111222', '12122222', '22222222', '12673939']

for testCase in range(1, TC+1):
    # nums = list(map(int, list(input().rstrip())))
    nums = list(map(int, list(numsList[testCase-1])))
    cache = [-1] * (len(nums)+1)
    print(memorize(0))