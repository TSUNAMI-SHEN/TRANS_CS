# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_ = x + y + carry

            carry = sum_ // 10
            sum_ = sum_ % 10
            cur.next = ListNode(sum_)

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry == 1:
            cur.next = ListNode(1)
        
        return dummy.next
