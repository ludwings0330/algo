'''
두 문자열 A, B A에 연산을 최소 횟수로 수행해 B로 만든다.


1. A의 한 위치에 문자를 하나 삽입
2. A의 문자를 하나 삭제
3. A의 문자 하나를 다른 문자로 교체

두 문자열이 주어졌을 때, 최소 편집 횟수를 구하시오.

asdfasd
fasdfff

'''


import sys
input = lambda: sys.stdin.readline().rstrip()

A = list(input())
B = list(input())
