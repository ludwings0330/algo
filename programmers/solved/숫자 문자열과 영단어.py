numbers = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6",
           "seven":"7", "eight":"8", "nine":"9"}


def solution(s):
    # 1<= s <= 50
    answer = []
    index = 0
    origin_length = len(s)

    while index < origin_length:
        if s[index].isdigit():
            answer.append(s[index])
            index += 1
        else:
            for number in numbers.keys():
                if s[index:index + len(number)] == number:
                    index += len(number)
                    answer.append(numbers[number])
                    break

    return int(''.join(answer))


ss = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
results = [1478, 234567, 234567, 123]

for i, s in enumerate(ss):
    print("input : {} \nexpect : {} \nmy_answer : {}".format(s, results[i], solution(s)))

