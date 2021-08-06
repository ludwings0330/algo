# Title : 1의 갯수 세기
# Tag : 비트, 누적합


import sys
input = lambda: sys.stdin.readline().rstrip()

def funcCount(x):
    ret = x & 1 # 제일 오른쪽 bit이 1인지 0인지 확인
    for i in range(54, 0, -1):
        if x & (1 << i):
            ret += d[i-1] + (x - (1 << i) +1)
            x -= 1 << i
    return ret


d = [1]
for i in range(1, 55):
    d.append(d[i-1]*2 + (1<<i))
A, B = map(int, input().split())
print(funcCount(B) - funcCount(A-1))