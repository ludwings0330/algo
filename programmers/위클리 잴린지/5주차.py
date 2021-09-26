# Title : 모음 사전
# Tag : 재귀


import sys

vo = ['', 'A', 'E', 'I', 'O', 'U']
word_dict = {}
for i, ch in enumerate(vo):
    word_dict[i] = ch
    word_dict[ch] = i

ch_list = [''] * 5
mark = 0
data_dict = {}

def alpha_up():
    global mark
    ch = ch_list[mark]
    if ch == '':
        # 빈칸이었으면 높여주고 옆으로 이동.
        ch_list[mark] = word_dict[(word_dict[ch] + 1) % 6]

        mark = min(mark + 1, 4)
    elif ch == 'U':
        # 마지막이면 여긴 빈칸이 되고, 앞의 수를 한개 올려준다.
        ch_list[mark] = ''
        mark = max(mark - 1, 0)
        alpha_up()
    else:
        ch_list[mark] = word_dict[(word_dict[ch] + 1) %6]
        mark = min(mark + 1, 4)

def make(f):
    global mark
    mark = 0
    rank = 1
    made_str = 'START'

    while made_str != f:
        alpha_up()

        made_str = ''.join(ch_list)
        data_dict[made_str] = rank
        rank += 1


def solution(word):
    make(word)
    return data_dict[word]

print(solution(input()))
# word = ['AAAAE', 'AAAE', 'I', "EIO"]
# for w in word:
#     print(solution(w))