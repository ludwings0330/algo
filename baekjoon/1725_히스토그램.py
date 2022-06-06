import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heights = [int(input()) for _ in range(N)]


def solve(left, right):

    # base case
    if left == right:
        return heights[left]

    mid = (left + right) // 2

    ret = max(solve(left, mid), solve(mid + 1, right))

    ll = mid
    rr = mid+1

    length = 2
    height = min(heights[ll], heights[rr])
    ret = max(ret, height * length)

    # 둘중 더 높은 것을 선택해야한다.
    while left < ll or rr < right:
        # 더 높은쪽 울타리로 확장하는 것이 답이 될 수 있기 때문에
        # 오른쪽 울타리가 더 높으면 오른쪽을 우선으로 확장한다
        if rr < right and (ll == left or heights[ll-1] < heights[rr + 1]):
            rr += 1
            height = min(height, heights[rr])
        # 그 외의 경우라면 왼쪽으로 확장한다.
        else:
            ll -= 1
            height = min(height, heights[ll])
        length += 1
        ret = max(ret, height * length)

    return ret


print(solve(0, N-1))
