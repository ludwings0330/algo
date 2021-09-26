C = int(input())

def solve(left, right):
    # base case
    if left == right:
        return heights[left] * 1

    mid = (left + right) // 2

    # 최대 크기가 왼쪽에 있는 경우, 오른쪽에 있는 경우 중 큰 값을 선택해준다.
    ret = max(solve(left, mid), solve(mid+1, right))

    # 최대 크기가 중앙에 걸쳐져 있는 경우, 중앙에서 확장하면서 최대 높이를 구해준다.
    lo, hi = mid, mid + 1
    height = min(heights[lo], heights[hi])

    # 왼쪽으로 구간을 넓힐지, 오른쪽으로 구간을 넓힐지 선택한다.
    while left < lo or hi < right:
        if hi < right and (lo == left or heights[lo-1] < heights[hi + 1]):
            # 오른쪽으로 경계를 넓히는게 이득이므로 오른쪽으로 넓힌다.
            hi += 1
            # 둘중에 더 작은 값을 직사각형의 높이로 취할 수 있다.
            height = min(height, heights[hi])
        else:
            lo -= 1
            height = min(height, heights[lo])

        #높이와 밑변이 갱신되고 다시 최대 넓이를 구해본다.
        ret = max(ret, height * (hi - lo + 1))

    return ret
for testCase in range(1, C+1):
    N = int(input())
    heights = list(map(int, input().split()))

    print(solve(0, N-1))