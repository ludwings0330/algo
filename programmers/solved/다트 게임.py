
def solution(dartResult):
    answer = 0
    store = [0, 0, 0]

    index = 0
    for i, s in enumerate(dartResult):
        if s.isdigit():
            if s == '1' and dartResult[i+1] == '0':
                store[index] += 10
            else:
                store[index] += int(s)
                index += 1
            continue

        if s == 'D':
            store[index-1] **= 2
        elif s == 'T':
            store[index-1] **= 3

        if s == '*':
            store[index-1] *= 2
            if index-2 > -1:
                store[index-2] *= 2
        elif s == '#':
            store[index-1] *= -1

    return sum(store)

dartResult = ["1S2D*3T",
                "1D2S#10S",
                "1D2S0T",
                "1S*2T*3S",
                "1D#2S*3S",
                "1T2D3D#",
                "1D2S3T*"]

for d in dartResult:
    print(solution(d))