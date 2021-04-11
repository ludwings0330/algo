def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    check_list = []

    for user_skill in skill_trees:
        user_skill_list = list(user_skill)
        for x in range(len(user_skill_list)):
            if user_skill_list[x] not in skill_list:
                user_skill_list[x] = ''

        check_list.append(''.join(user_skill_list))

    for check in check_list:
        flag = True
        for c in range(len(check)):
            if check[c] != skill[c]:
                flag = not flag
                break
        if flag:
            answer += 1
    return answer

if __name__ == "__main__":
    skill, skill_trees = "CBD", ["BACDE", "CBADF", "AECB", "BDA"]
    print("answer is {}".format(solution(skill, skill_trees)))