from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dq = deque()

        if not head:
            return True

        node = head

        while node is not None:
            dq.append(node.val)
            node = node.next

        while len(dq) >= 1:
            if dq[0]==dq[-1]:
                dq.popleft()
                dq.pop()
            else:
                return False

        return True


