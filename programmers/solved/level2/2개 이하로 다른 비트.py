# 1 <= len(numbers) <= 100,000
# 0 <= numbers <= 10 ** 15

# x 보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수 찾기

def solution(numbers):
    answer = []
    for number in numbers:
        binary_number = []
        while number:
            binary_number.append(number%2)
            number //= 2

        binary_number.append(0)

        for i, b in enumerate(binary_number):
            if b == 0:
                binary_number[i] = 1
                if i != 0:
                    binary_number[i-1] = 0
                break

        tmp = 0
        for i, b in enumerate(binary_number):
            tmp += 2**i * b
        answer.append(tmp)
    return answer


numbers = [2, 7]
print(solution(numbers))
