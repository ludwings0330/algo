def solution(seoul):
    answer = "김서방은 {}에 있다"
    position = seoul.index("Kim")

    return answer.format(position)

print(solution(["Jane", "Kim"]))