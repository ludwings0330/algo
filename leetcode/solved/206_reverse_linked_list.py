class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # linked list를 역순으로 만들기
        node = head
        prev = None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
