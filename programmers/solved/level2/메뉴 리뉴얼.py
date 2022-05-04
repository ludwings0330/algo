# 새로운 메뉴 구성
# 최소 2가지 이상의 단품메뉴로 코스요리 제공
# 최소 2명 이상의손님으로부터 주문된 단품메뉴 조합에 대해서만 코스 요리 메뉴 후보에 포함
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    check_course_number = [True if i in course else False for i in range(21)]
    answer = []
    course_dict = {}
    length_list = [0] * 21
    for order in orders:
        menus = list(order)
        menus.sort()
        for i in range(2, len(menus)+1):
            combinations_list = list(combinations(menus, i))
            for combination in combinations_list:
                course_made = ''.join(combination)
                if course_made in course_dict:
                    course_dict[course_made] += 1
                    length_list[len(course_made)] = max(length_list[len(course_made)], course_dict[course_made])
                else:
                    course_dict[course_made] = 1
                    length_list[len(course_made)] = max(length_list[len(course_made)], course_dict[course_made])

    for key in course_dict.keys():
        l = len(key)
        if check_course_number[l] and length_list[l] >= 2 and length_list[l] == course_dict[key]:
            answer.append(key)

    return sorted(answer)


# 2 <= orders <= 20
# 각 문자열은 2 이상 10 이하인 문자열
# 20개 10 개
orders = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
          ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
          ["XYZ", "XWY", "WXA"]]
courses = [[2, 3, 4], [2, 3, 5], [2, 3, 4]]

for order, course in zip(orders, courses):
    print(solution(order, course))