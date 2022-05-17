def solution(m, musicinfos):
    answer = [["", 0]]

    for music_info in musicinfos:
        start_time, end_time, title, melody = music_info.split(",")
        start_time = int(start_time.split(":")[0]) * 60 + int(start_time.split(":")[1])
        end_time = int(end_time.split(":")[0]) * 60 + int(end_time.split(":")[1])
        play_time = end_time - start_time

        melody_tmp = []
        for c in list(melody):
            if c != '#':
                melody_tmp.append(c)
            else:
                melody_tmp[-1] += '#'

        melody_list = []

        while len(melody_list) < play_time:
            melody_list.extend(melody_tmp)

        played_melody = ''.join(melody_list[:play_time])

        if m in played_melody:
            played_melody = played_melody.replace(m, '@').replace('@#', '')

            if '@' in played_melody and answer[0][1] < play_time:
                answer[0] = [title, play_time]

    return answer[0][0] if answer[0][0] != '' else '(None)'

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# print(solution(m, musicinfos))

m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))

m = "CCB"
musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
print(solution(m, musicinfos))
