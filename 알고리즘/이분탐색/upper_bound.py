# 이진 탐색의 변형으로 중복된 자료가 있을 때 유용하게 사용할 수 있는 탐색 알고리즘
# Target 값보다 큰 값이 나오는 위치를 찾는 알고리즘
# target 값을 초과하는 정수의 위치를 찾는 문제

# 시간 복잡도 O(logN)
def upper_bound(arr, target):
    left = mid = 0
    # 마찬가지로 범위는 left <= index <= right 이니까 index 로 len -11 로 둔다.
    right = len(arr) - 1

    # right = mid 로 두기 때문에, left <= right 조건이라면 무한 루프에 빠질 수 있다.
    # arr[mid] >= target 일때 빠져나오기 위해서 left < right 를 주어야한다.
    while left < right:
        mid = (left + right) // 2

        # target 보다 같거나 작으면 arr[mid] 는 가능성이 없는 수 이므로 left = mid + 1 로 둔다
        # target 값보다 커야하기 때문에 target과 같으면 제외 해주어야 한다. 따라서 arr[mid] == target 일때, left = mid + 1
        if arr[mid] <= target:
            left = mid + 1
        # 크거나 같으면 정답 가능성이 있기 떄문에 mid + 1 이 아니라, right = mid 로 둔다.
        elif arr[mid] > target:
            right = mid

    ret = right

    return ret


arr = [1, 1, 2, 3, 4, 5, 5, 5, 10, 12, 113, 23,13,15, 16, 179, 23, 33, 45, 98, 83, 73,11, 23]
arr.sort()
print(arr)
index = upper_bound(arr, 5)
print(index, arr[index-1], arr[index], arr[index + 1])
