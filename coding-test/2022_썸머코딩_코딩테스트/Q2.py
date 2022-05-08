# 사무실이 여러층에 나누어져 있음
# 사무실은 호수로 구분, 사무실마다 직원 자리가 있음
# 직원들은 지정된 자리를 하나 이상 사용, 한 사람이 한 사무실에 지정된 자리를 두개 이상 사용하지 않음
# 새 자리가 생겻을때 한사람에게 자리를 준다

# 해당 방에 이미 지정 자리가 있는 직원 제외
# 지정 자리가 제일 적은 직원 먼저 할당
# 지정 자리 개수가 동일하면 가까운 방
# 거리가 똑같으면 이름으로 비교


# 새 자리를 받을 수 있는 사람들을 우선 순위가 높은 사람부터 순서대로 배열에 담아 return

# 101 <= room number <= 9999
# 1 <= 사람수 100,000

from collections import defaultdict

def get_dist(rooms, target):
    return min([abs(room - target) for room in rooms])

def parse_room_data(data):
    room_number = int(data[1:data.find(']')])
    names = data[data.find(']') + 1 :].split(',')
    return room_number, names


def solution(rooms, target):
    answer = []
    person_info = defaultdict(list)
    excluded = []

    for room in rooms:
        room_number, names = parse_room_data(room)

        if room_number == target:
            excluded = names

        for name in names:
            person_info[name].append(room_number)

    for name in excluded:
        del(person_info[name])

    person_list = []
    for name in person_info:
        person_list.append([name, len(person_info[name]), get_dist(person_info[name], target)])

    person_list.sort(key = lambda x: (x[1], x[2], x[0]))
    return [person[0] for person in person_list]


rooms = [["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"],
         ["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"],
         ["[1234]None,Of,People,Here","[5678]Wow"]]
targets = [403, 202, 1234]

for room, target in zip(rooms, targets):
    print(solution(room, target))
