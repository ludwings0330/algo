# title : Array with elements not equal to average of neighbors
def solution(nums):
    ret = []
    nums.sort()
    l = len(nums)
    left = 0
    right = l - 1
    while left <= right:
        if left == right:
            ret.append(nums[left])
        else:
            ret.append(nums[left])
            ret.append(nums[right])
        left += 1
        right -= 1


    return ret

print( solution([6,2,0,9,7]) )
