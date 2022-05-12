class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ret = ListNode()

        odd_root = odd = ListNode()
        even_root = even = ListNode()

        isOdd = True
        while head:
            if isOdd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            isOdd ^= True

            head = head.next

        even.next = None
        odd.next = even_root.next
        return odd_root.next


root = head = ListNode()
l1 = [2, 1, 3, 5, 6, 4, 7]
prev = None

for n in l1:
    current = ListNode(n)
    head.next = current
    head = head.next

print(Solution().oddEvenList(root.next))
