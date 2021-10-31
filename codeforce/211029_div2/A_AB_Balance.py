'''
문자열 s : 길이는 n 이고, a 또는 b 로 이루어져 있음
AB(s) : ab 가 나오는 횟수
BA(s) : ba가 나오는 횟수
index i 를 골라서 a 또는 b로 바꿀수 있다.

minimum number of steps to make to achieve AB(s) = BA(s)?

최소 횟수로 AB(s) = BA(s)를 만드는 변환된 문자열 s를 출력하라.

1<=len(s)<=100

1. 최초 문자열 s 에서 AB(s) 와 BA(s) 를 구한다.
2. 같으면 그대로 출력, 다르면 변환
3. 변환은 어떻게? 많은걸 줄이거나, 적은걸 늘린다.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()

TC = int(input())

def AB(s):
    ret = 0
    for i in range(1, len(s)):
        if s[i-1] == 'a' and s[i] == 'b':
           ret += 1
    return ret

def BA(s):
    ret = 0
    for i in range(1, len(s)):
        if s[i-1] == 'b' and s[i] == 'a':
           ret += 1
    return ret

while TC:
    TC -= 1
    s = list(input())
    ab = AB(s)
    ba = BA(s)

    if ab == ba:
        print(''.join(s))
    else:
        s[-1] = s[0]
        print(''.join(s))


