# 대소문자, 숫자, 공백, 마침표, 빼기부호
#head, number, tail
def solution(files):
    answer = []
    for file in files:
        head = []
        number = []
        tail = ""

        for i, ch in enumerate(file):
            if '0' <= ch <= '9':
                number.append(ch)
            else:
                if i > 0 and file[i-1].isdigit():
                    tail = file[i:]
                    break
                else:
                    head.append(ch)
        answer.append([''.join(head), ''.join(number), tail])
    answer.sort(key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in answer]


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG", "ims2"]
print(solution(files))
