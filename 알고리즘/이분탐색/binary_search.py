def binarySearch(arr, target):
    ret = -1

    left = 0
    # left <= index <= right 이기 때문에 -1 을 해주어야한다.
    # -1을 해주지 않으면 최대값을 초과하는 값을 탐색했을때 index Error
    right = len(arr) - 1

    # target 값이 left 혹은 right 위치에 있을 수 있다.
    # left == right 일때, mid == left == right 가 된다.
    while left <= right:
        mid = (left + right) // 2

        # 존재하면 해당 index 반환
        if arr[mid] == target:
            ret = mid
            break
        # Target 값이 더 작으면 right 를 줄여야함
        elif target < arr[mid]:
            right = mid - 1
        # Target 값이 더 크면 left 를 키워야함
        elif target > arr[mid]:
            left = mid + 1

    # 존재하지않으면 -1 반환, 존재하면 해당 index 반환
    return ret


arr = [1, 2, 2, 3, 4, 10, 11, 15, 28, 25, 30]
arr.sort()

print(binarySearch(arr, 100))