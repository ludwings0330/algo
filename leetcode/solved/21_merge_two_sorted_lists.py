from typing import Optional
import sys
sys.setrecursionlimit(10**9)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        # head = ListNode()
        # tmp_head = head
        #
        # while list1 is not None or list2 is not None:
        #     if list1 is None:
        #         tmp_head.next = list2
        #         list2 = list2.next
        #         tmp_head = tmp_head.next
        #         continue
        #
        #     if list2 is None:
        #         tmp_head.next = list1
        #         list1 = list1.next
        #         tmp_head = tmp_head.next
        #         continue
        #
        #     if list1.val < list2.val:
        #         tmp_head.next = list1
        #         tmp_head = tmp_head.next
        #         list1 = list1.next
        #     else:
        #         tmp_head.next = list2
        #         tmp_head = tmp_head.next
        #         list2 = list2.next
        #
        # return head.next
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

