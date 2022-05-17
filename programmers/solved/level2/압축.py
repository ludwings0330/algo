dictionary = {}

for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    dictionary[ch] = i + 1


# LZW 압축
def solution(msg):
    answer = []
    s, e = 0, 1
    msg += "@"
    while s < len(msg)-1:
        e = s
        while e < len(msg):
            e += 1
            if msg[s:e] in dictionary:
                continue
            else:
                answer.append(dictionary[msg[s:e-1]])
                dictionary[msg[s:e]] = len(dictionary) + 1
                s = e - 1
                break

    return answer

