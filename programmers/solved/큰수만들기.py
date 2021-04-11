def solution(number, k):
    answer = []
    index = 0
    #

    while k > 0:
        max = index
        for i in range(index, index+k+1):
            if i >= len(number):
                index = -1
                break
            if number[max] < number[i] and number[max] != number[i]:
                max = i
            if number[max] == '9':
                break

        if index == -1:
            break
        answer.append(number[max])
        k -= (max-index)
        index += (max-index)+1



    answer = ''.join(answer) + number[max+1:]
    return answer


if __name__ == "__main__":
    #number, k = input().split()
    number = "21"
    k = 1
    #775841
    print(solution(number, k))