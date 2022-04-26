import sys
input = lambda: sys.stdin.readline().rstrip()


def solution2(s):
    answer = origin_length = len(s)
    answer_str = ""
    for unit in range(1, len(s)//2 + 1):
        unit_list = []

        base = 0
        count = 1

        for step in range(unit, origin_length + unit, unit):
            is_duplicate = True
            for k in range(unit):
                if k + step >= origin_length:
                    is_duplicate = False
                    break
                if s[base+k] != s[k + step]:
                    is_duplicate = False
                    break
            if is_duplicate:
                count += 1
            else:
                if count > 1:
                    unit_list.append(str(count))
                unit_list.append(s[base:base+unit])
                base = step
                count = 1
        if answer > len(''.join(unit_list)):
            answer_str = ''.join(unit_list)
        answer = min(answer, len(''.join(unit_list)))
    print(answer_str)
    return answer


# s <= 1000
# 압축된 최소 길이 출력
def solution(s):

    answer = origin_length = len(s)

    # 1, 2, 3, 4, ... len(s)//2 로 쪼개기
    for unit in range(1, len(s)//2+1):
        current_length = origin_length

        base = 0
        count = 1

        for step in range(unit, origin_length+unit, unit):
            is_duplicate = True
            for k in range(unit):
                if k+step >= origin_length:
                    is_duplicate = False
                    break

                if s[base + k] != s[k + step]:
                    is_duplicate = False
                    base = step
                    break

            if is_duplicate:
                count += 1
            else:
                digit = 0
                current_length = current_length - (count-1)*unit

                if count > 1:
                    while count > 0:
                        digit += 1
                        count //= 10
                        current_length += 1
                count = 1
                answer = min(answer, current_length)
    return answer


ss = ["xxxxxxxxxxyyy", "abcabcabcdabcfabcabcabczabcabcdddabc", "werwerwsdgsdfsdfsdf", "cccccccccccc", "aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
results = [5, 27, 15, 3, 7, 9, 8, 14, 17]

isOk = True
for i, s in enumerate(ss):
    print(" test case({})".format(i))
    print("input : " + s)
    print("expect : {}".format(results[i]))
    print("my answer : {}".format(solution(s)))
    print("my answer2 : {}".format(solution2(s)))
