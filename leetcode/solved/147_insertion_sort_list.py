class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        current = root = ListNode(0)

        while head:
            while current.next and current.next.val < head.val:
                current = current.next

            tmp = head.next
            head.next = current.next
            current.next = head
            head = tmp


            if head and current.val > head.val:
                current = root

        return root.next


current = root = ListNode()
number = [4, 2, 1, 3]
for n in number:
    current.next = ListNode(n)
    current = current.next
print(Solution().insertionSortList(root.next))