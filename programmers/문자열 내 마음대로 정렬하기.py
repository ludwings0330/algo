def solution(strings, n):
    return sorted(sorted(strings), key = lambda x: x[n])


strings = [["sun", "bed", "car"], ["abce", "abcd", "cdx"]]
nn = [1, 2]

for i in range(len(strings)):
    print(solution(strings[i], nn[i]))
