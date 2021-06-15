#전화번호 목록
import sys
input = sys.stdin.readline

TC = int(input())

class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

while TC:
    TC -= 1
    numbers = []
    n = int(input())
    Head = Node(key = '')

    isOverlap = False

    for _ in range(n):
        number = input().rstrip()
        numbers.append(number)
        l = len(number)
        node = Head

        if not isOverlap:
            for i, key in enumerate(number):
                if key in node.children:
                    if node.children[key].data != None or i == l-1:
                        isOverlap = True
                        break
                    node = node.children[key]
                    continue
                else:
                    node.children[key] = Node(key = key)
                    node = node.children[key]
                if i == l-1:
                    node.data = number
    if isOverlap:
        print('NO')
    else:
        print('YES')