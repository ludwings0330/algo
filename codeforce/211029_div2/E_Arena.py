'''
n 명의 영웅
ai -> 체력

라운드 시작할때 각 영웅이 다른 모든 영웅한테 1의 damage를 입힌다. 1보다 적은 hp면 사망한다.
라운드가 끝낫을때, 1명남아있으면 승리, 아니면 승리 없음

1 <= ai <= x 인 방법의 수를 구하는 것 winner가 없도록

MOD = 998244353

n, x : 영웅수 n
        체력 상한선x
'''


import sys
input = lambda:sys.stdin.readline().rstrip()

n, k = map(int, input().split())

def solve(r):
    pass