import sys
input = lambda:sys.stdin.readline().rstrip()

T = int(input())


'''
1x1 A개
2x1 B개
ㄴ자모양 C개
로 세로가 2인 직사각형을 만들 수 있는가?
회전 시킬 수 없다

'''

while T:
    A, B, C = map(int, input().split())

    if A < C:
        print('No')
    else:
        A = A - C
        if C != 0:
            if A % 2 == 0:
                print('Yes')
            else:
                print('No')
        else:
            if (B%2 == 0 and A%2 == 0) or (B%2 == 1 and A>=2 and A%2 == 0):
                print('Yes')
            else:
                print('No')
    T -= 1