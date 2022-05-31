def merge_sort(arr):
    if len(arr) == 1:
        return arr

    n = len(arr)
    left = merge_sort(arr[:n//2])
    right = merge_sort(arr[n//2:])

    ret = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1

    return ret + left[l:] + right[r:]

print(merge_sort([4, 3, 1, 2]))