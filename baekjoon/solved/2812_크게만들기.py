import sys
input = lambda: sys.stdin.readline().rstrip()


N, K = map(int, input().split())
num = list(input())

'''
N 자리 숫자 num,
K 개를 지웠을 때 얻을 수 있는 가장 큰 수 출력

맨 앞자리부터,
1. 뒷자리가 더 크면
    1.1 현재 자리를 지운다.
    
2. 뒷자리가 더 작으면
    - 현재는 내버려 두고 다음 자리로 넘어간다.
뒷자리가 더 크다면 지운다.
'''

stack = [num[0]]

for i in range(1, N):
    if stack[-1] < num[i]:
        if K > 0:
            while stack and stack[-1] < num[i] and K > 0:
                K -= 1
                stack.pop()
            stack.append(num[i])
        else:
            stack.append(num[i])
            continue

    else:
        stack.append(num[i])
while K:
    K-= 1
    stack.pop()
print(''.join(stack))
