import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())
def get_F(start, end, k):
    ret = 0

    for i in range(start, end):
        ret += magnet[i][1] / ((k - magnet[i][0])**2)
    return ret
def solve(i):
    left = magnet[i][0]
    right = magnet[i+1][0]
    before = -1
    # 0~i , i+1~N-1
    while left < right:
        k = (left + right)/2
        if round(k, 12) == round(before, 12):
            break
        left_sum = get_F(0, i+1, k)
        right_sum = get_F(i+1, N, k)
        if left_sum == right_sum:
            break
        elif left_sum > right_sum:
            left = k
        else:
            right = k
        before = k
    return k
for test_case in range(1, TC+1):

    print("#{0}".format(test_case), end=' ')
    N = int(input())
    input_list = list(map(int, input().split()))
    magnet = []
    for i in range(N):
        magnet.append([input_list[i], input_list[i+N]])

    magnet.sort()

    for i in range(N-1):
        ans = solve(i)
        print("{:.10f}".format(ans), end=' ')

    print()