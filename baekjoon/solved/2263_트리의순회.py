import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
inorderDict = dict()

for i in range(n):
    inorderDict[inorder[i]] = i
postorder = list(map(int, input().split()))
preorder = []

def solution(lenInorder, lenPostorder):
    if  (lenPostorder[1] - lenPostorder[0] < 0): # 둘중에 하나라도 없으면 끝냄
        return
    root = postorder[lenPostorder[1]]
    rootindex = inorderDict[root]
    preorder.append(root)

    inorderLeft = [lenInorder[0], rootindex - 1]
    inorderRight = [rootindex+1, lenInorder[1]]
    postorderLeft = [lenPostorder[0], lenPostorder[0] + (rootindex - lenInorder[0]) - 1]
    postorderRight = [lenPostorder[0] + (rootindex - lenInorder[0]), lenPostorder[1] -1]

    solution(inorderLeft, postorderLeft)
    solution(inorderRight, postorderRight)

solution([0, len(inorder)-1], [0, len(postorder)-1])

print(' '.join(str(_) for _ in preorder))

