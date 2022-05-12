class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self,head: ListNode) -> ListNode:
        # node = head
        #
        # while node and node.next is not None:
        #     node.val, node.next.val = node.next.val, node.val
        #     node = node.next.next
        #
        #
        # return head

        # ret = prev = ListNode()
        # prev.next = head
        #
        # while head and head.next is not None:
        #     b = head.next
        #     head.next = b.next
        #     b.next = head
        #
        #     prev.next = b
        #
        #     head = head.next
        #     prev = prev.next.next
        #
        # return ret.next

        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p

        return head
