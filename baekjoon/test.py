import sys

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
# inorder :  중위순회 왼쪽, 중간, 오른쪽
# postorder : 후위 순회 왼쪽, 오른쪽, 중간
# preorder : 중간, 왼쪽, 오른쪽
preorder = []

def solution(inorder, postorder):
    if not (inorder and postorder):
        return

    root = postorder[-1]
    preorder.append(root)

    rootIndex = inorder.index(root)
    inorderLeft = inorder[:rootIndex]
    postorderLeft = postorder[:len(inorderLeft)]

    inorderRight = inorder[rootIndex+1:]
    postorderRight = postorder[len(inorderLeft):-1]

    solution(inorderLeft, postorderLeft)
    solution(inorderRight, postorderRight)

solution(inorder, postorder)
print(' '.join(str(_) for _ in preorder))


