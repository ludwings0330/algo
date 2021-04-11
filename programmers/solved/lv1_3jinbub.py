def solution(n):
    answer = 0

    number_list = []


    while n>=3:
        number_list.append(int(n % 3))
        n = n / 3

    number_list.append(int(n))
    number_list.reverse()

    print(number_list)

    for i in range(len(number_list)):
        answer += number_list[i] * (3**i)

    return answer



if __name__ == "__main__":
    solution(125)