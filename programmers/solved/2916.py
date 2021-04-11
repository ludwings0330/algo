def solution(a, b):
    answer = ''
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    arr = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    day = 0
    for i in range(1, a):
        day += mon[i]

    day += b
    day %= 7

    answer = arr[day]

    return answer


if __name__ == "__main__":
    a = 5
    b = 24
    d = solution(a,b)
    print(d)