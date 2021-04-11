def solution(numbers, hand):
    answer = ''
    rhand = 12
    lhand = 10

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            lhand = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            rhand = num
        else :
            if num == 0:
                num = 11

            l_len = 0
            n = abs(num-lhand)
            while n >= 3:
                l_len += 1
                n = abs(n-3)
            l_len += n

            r_len = 0
            n = abs(num-rhand)
            while n >= 3:
                r_len += 1
                n = abs(n-3)
            r_len += n

            if l_len < r_len:
                answer +="L"
                lhand = num
            elif l_len == r_len:
                if hand == "right":
                    answer +="R"
                    rhand = num
                else:
                    answer +="L"
                    lhand = num
            else :
                answer +="R"
                rhand = num
    print(answer)
    return answer

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = "right"
    solution(numbers, hand)


    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = "left"
    solution(numbers, hand)


    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand = "right"
    solution(numbers, hand)