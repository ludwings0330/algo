class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = nodes = ListNode()


        carry = 0
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, val = sum//10, sum%10
            nodes.next = ListNode(val)
            nodes = nodes.next

        if carry > 0:
            nodes.next = ListNode(carry)

        return ret.next