import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

def solve(left, right):
    if left == right:
        return H[left]

    mid = (left + right)//2
    ret = max(solve(left, mid), solve(mid+1, right))

    lo = mid
    hi = mid + 1

    height = min(H[hi], H[lo])
    ret = max(ret, height*2)

    while left < lo or hi < right:
        if hi < right and (lo == left or H[lo - 1] < H[hi + 1]):
            hi += 1
            height = min(height, H[hi])
        else:
            lo -= 1
            height = min(height, H[lo])
            
    ret = max(ret, height * (hi - lo + 1))
    return ret

while TC:
    TC -= 1
    N = int(input())
    H = list(map(int, input().split()))

    print(solve(0, N-1))

# 3
# 7
# 7 1 5 9 6 7 3
# 7
# 1 4 4 4 4 1 1
# 4
# 1 8 2 2
