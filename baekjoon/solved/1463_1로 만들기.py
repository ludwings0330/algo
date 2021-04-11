# 1. X가 3으로 나누어 떨어지면 3로 나누기
# 2. X가 2로 나누어 떨어지면 2로 나누기
# 3. 1빼기
# 1.5초 이내
# 1 <= N <= 10^6
# 세개의 연산 사용해서 1만들기. 연산 횟수의 최솟값 출력.1000000
if __name__ == "__main__":
    N = int(input())
    count = 0
    arr = [0]*1000001

    for i in range(2, N+1):
        arr[i] = arr[i-1] + 1
        # i-1 에서 i로 가는 방법은 3. 방법 사용
        if i%2 == 0:
            arr[i] = min(arr[i//2] + 1, arr[i])
            # 2로 나누어지는 경우 밑에서 끌어올림.
        if i%3 == 0:
            arr[i] = min(arr[i], arr[i//3] + 1)
    print(arr[N])