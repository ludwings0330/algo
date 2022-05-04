# left <= right
# 약수의 갯수가 짝수 수는 더하고, 약수의 갯수가 홀수인 수는 뺀 수를 return


def count_divisor(number):
    count = 0
    if number == 1:
        return 1
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    return count


def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        num_of_divisor = count_divisor(number)
        if num_of_divisor % 2 == 1:
            answer -= number
        else:
            answer += number

    return answer


print(solution(13, 17))
print(solution(24, 27))
print(solution(1, 1))


for i in range(13, 18):
    print(count_divisor(i))
for i in range(24, 28):
    print(count_divisor(i))