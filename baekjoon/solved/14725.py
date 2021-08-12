# title ; 개미굴
# tag ; 트라이, 자료구조

import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
    def __init__(self, key):
        self.key = key
        self.child = dict()

class Trie:
    def __init__(self):
        self.head = Node(None)

    def update(self, data):
        node = self.head
        for room in data:
            if room not in node.child:
                node.child[room] = Node(room)
            node = node.child[room]

    def print_items(self, depth, node):
        if node == None:
            node = self.head
        for c in sorted(node.child.keys()):
            print('--'*depth, c, sep='')
            self.print_items(depth+1, node.child[c])


N = int(input())
trie = Trie()
for _ in range(N):
    String = input().split()
    trie.update(String[1:])

trie.print_items(0, None)
