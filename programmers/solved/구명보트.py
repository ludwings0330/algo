def solution(people, limit):
    answer = 0

    people.sort(reverse = True)
    # 내림차순 정렬
    # 무조건 2명씩 나가도록
    n = len(people)
    head = 0
    tail = n-1

    while head <= tail:
        if head == tail:
            answer += 1
            break
        elif people[head] + people[tail] <= limit:
            head += 1
            tail -= 1
            answer += 1
        else:
            head += 1
            answer += 1

    return answer

if __name__ == "__main__":
    people = [70, 50, 80, 50]
    limit = 100

    print("answer is {}".format(solution(people, limit)))