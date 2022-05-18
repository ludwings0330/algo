import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
for test_case in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    for i in range(1, len(a)):
        a[i] += a[i-1]

    for query in range(q):
        target = int(input())
        answer = -1

        l, r = 0, len(a)
        while l < r:
            mid = (l + r) // 2

            if a[mid] < target: # 정답 가능성 없음 -> mid를 더 키워야함 -> left 증가
                l = mid + 1
            else: # target <= a[mid] -> 정답 가능성 있음 -> mid를 더 작게해서 아래쪽에서 답이있는지 확인 -> right 감소
                r = mid
        answer = answer if r == len(a) else r + 1
        print(answer)