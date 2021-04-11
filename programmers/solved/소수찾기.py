# 종이조각으로 만들수 있는 소수의 갯수 return
# numbers 길이 1<=len(numbers)<= 7
# numbers 는 0~9 의 숫자

def solution(numbers):
    from itertools import permutations
    test = {''}

    answer = 0
    for i in range(1, len(numbers) + 1):
        test.update(list(map(''.join, permutations(numbers, i))))

    number_list = list(test)
    number_list = list(map(int, number_list[1:]))
    number_list = list(set(number_list))

    for i in number_list:
        if check(i):
           # print("{} 는 소수".format(i))
            answer += 1

    return answer

def check(number):
    if number == 2:
        return True
    elif number ==1 or number==0:
        return False
    for i in range(2,number):
        if number%i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = "011"

    print("answer is {}".format(solution(numbers)))