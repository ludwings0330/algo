def solution(n, arr1, arr2):
    answer = []

    answer_list = []

    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        answer_list.append(line)

    for i in range(n):
        tmp1 = arr1[i]
        tmp2 = arr2[i]
        for j in range(n):
            answer_list[i][j] = tmp1%2 + tmp2%2
            tmp1 = int(tmp1 / 2)
            tmp2 = int(tmp2 / 2)

    for i in range(n):
        line = ""
        for j in range(n):
            if answer_list[i][n-1-j]>=1:
                line +="#"
            else:
                line +=" "

        answer.append(line)

    print(answer_list)
    print(answer)

    return answer

if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    solution(n, arr1, arr2)