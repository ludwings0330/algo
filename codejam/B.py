import sys
input = sys.stdin.readline

T = int(input())

def sol(i, toPick, arr):
    if len(arr) > 1:
        if int(arr[-2], 16) <= int(arr[-1], 16): # 이게 비감소 수열이야
            pass
        else:
            return

    if toPick == 1:
        global ans
        arr.append(S[i:])
        if int(arr[-2], 16) <= int(arr[-1], 16):
            pass
        else:
            arr.pop()
            return
        ans += 1
        arr.pop()
        return

    for j in range(i+1, len(S)):
        arr.append(S[i:j])
        sol(j, toPick-1, arr)
        arr.pop()

while T:
    T -= 1
    S = input().rstrip()

    ans = 1 # k == 1 인 경우 무조건

    for k in range(2, len(S)+1):
        sol(0, k, [])
    print(ans)