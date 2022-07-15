# import re
#
# N = int(input())
# for _ in range(N):
#     s = input()
#     s = re.sub("\^{3,}", "^^", s)
#     s = re.sub("\^.\^", "^_^", s)
#     s = re.sub("\(+", "(", s)
#     s = re.sub("\)+", ")", s)
#     print(s)

N = int(input())
for _ in range(N):
    ans = []
    s = input()
    for i in range(len(s)):
        if i == 0:
            ans.append(s[i])
            continue

        elif s[i] == '(':
            if ans[-1] == '(':
                continue
            ans.append(s[i])
        elif s[i] == ')':
            if ans[-1] == ')':
                continue
            ans.append(s[i])
        elif len(ans) > 1 and s[i] == '^':
            if ans[-1] == ans[-2] == '^':
                continue
            elif s[i-2] == '^':
                ans[-1] = '_'
            ans.append(s[i])
        else:
            ans.append(s[i])
    print(''.join(ans))
