N = int(input())
M = int(input())
S = input()


P = ['I', 'O'] * N + ['I']
NP = len(P)

s = 0
e = len(P)
answer = 0

flag = True
while e < M:
    flag = True
    for si, i in enumerate(range(s, e)):
        if P[si] != S[i]: # 틀렸으면 s와 e를 수정
            if i != s:
                s = i
                e = s+NP
            else:
                s += 1
                e += 1
            flag = False
            break
    if not flag: #실패했으면 다시돌아
        continue
    # 만약 참이야
    answer += 1
    a = e
    while a+1 < M and S[a] == 'O' and S[a+1] == 'I':
        answer += 1
        a += 2
    s = a
    e = s + NP
print(answer)