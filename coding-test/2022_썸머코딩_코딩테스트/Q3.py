# 왼손검지 Q, 오른손 검지 P
# 가까운 맨하탄거리의 손가락으로 누른다.

from collections import deque

left_side = list("12345QWERT")
right_side = list("67890YUIOP")


def get_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_horizontal_distance(pos1, pos2):
    return abs(pos1[1] - pos2[1])


def is_left_side(ch):
    return ch in left_side


def solution(line):
    answer = []
    #[row, col]
    pos_dict = {}

    for i, c in enumerate(list("1234567890")):
        pos_dict[c] = (0, i)
    for i, c in enumerate(list("QWERTYUIOP")):
        pos_dict[c] = (1, i)

    left_hand = 'Q'
    right_hand = 'P'

    for ch in line:
        tmp = 0

        left_dist = get_distance(pos_dict[left_hand], pos_dict[ch])
        right_dist = get_distance(pos_dict[right_hand], pos_dict[ch])

        if left_dist < right_dist:
            tmp = 0
            left_hand = ch
        elif left_dist > right_dist:
            tmp = 1
            right_hand = ch
        elif left_dist == right_dist:
            left_h_dist = get_horizontal_distance(pos_dict[left_hand], pos_dict[ch])
            right_h_dist = get_horizontal_distance(pos_dict[right_hand], pos_dict[ch])

            if left_h_dist < right_h_dist:
                tmp = 0
                left_hand = ch
            elif left_h_dist > right_h_dist:
                tmp = 1
                right_hand = ch
            elif left_h_dist == right_h_dist:
                if is_left_side(ch):
                    tmp = 0
                    left_hand = ch
                else:
                    tmp = 1
                    right_hand = ch

        answer.append(tmp)

    return answer
# 왼손 0, 오른손 1

line = ["Q4OYPI", "RYI76", "64E2"]
for li in line:
    print(solution(li))
