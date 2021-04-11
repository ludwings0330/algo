def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    answer.append(arr[0])
    del(arr[0])

    index = 0
    for num in arr:
        if num == answer[index]:
            continue
        else:
            answer.append(num)
            index+=1
    return answer


if __name__ == "__main__":
    arr =   [1, 1, 3, 3, 0, 1, 1]
    answer = solution(arr)
    print(answer)