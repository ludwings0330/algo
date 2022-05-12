class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if not head or left == right:
            return head

        root = start = ListNode()
        root.next = head

        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

        return root.next



root = head = ListNode()
l1 = [2, 1, 3, 5, 6, 4, 7]
prev = None

for n in l1:
    current = ListNode(n)
    head.next = current
    head = head.next

print(Solution().oddEvenList(root.next))