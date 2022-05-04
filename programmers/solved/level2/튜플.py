

def solution(s):
    answer = []
    board = [[]]
    s = s[1:-1].split(",{")

    for i in range(len(s)):
        s[i] = list(map(int, s[i].replace("{", '').replace("}", '').split(',')))

    s.sort(key = lambda x:len(x))

    print(s)
    answer = s[0]

    return answer


ss = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}",
      "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

for s in ss:
    print(solution(s))
