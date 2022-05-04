# 자연수 n이 매개변수로 주어진다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return
# 3 <= n <= 1,000,000

def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 1:
            answer = i
            break
    return answer


nn = [10, 12]
results = [3, 11]

for i in range(len(nn)):
    result = solution(nn[i])
    print("expected : ", results[i])
    print("my answer : ", result)