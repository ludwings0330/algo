def solution(record):
    answer = []
    users = dict()

    for input in record:
        line = ""
        input_list = input.split()
        action, uid, nick = '','',''

        action = input_list[0]
        uid = input_list[1]
        if len(input_list) == 3:
            nick = input_list[2]

        if action == 'Enter':
            line = "{}님이 들어왔습니다."
            if uid not in users: # 처음들
                users[uid] = [nick, str(len(answer))+","] # answer 몇 번째 줄에 있는지 저장
            else: # 처음이 아니야
                users[uid] = [nick, users[uid][1] + str(len(answer)) + ","]  # answer 몇 번째 줄에 있는지 저장

        elif action == 'Leave':
            line = "{}님이 나갔습니다."
            users[uid][1] = users[uid][1] + str(len(answer)) + ","
        else : # action == 'Change'
            users[uid][0] = nick
            continue
        answer.append(line)

    for uid in users:
        index_list = map(int, users[uid][1].split(',')[:-1])

        for index in index_list:
            answer[index] = answer[index].replace("{}", users[uid][0])

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan","Enter asdf uid1123",'Change asdf uid2215']

    print("answer is {}".format(solution(record)))