from typing import Optional


class ListNode:
    """Linked list node"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @ref: https://leetcode.com/problems/add-two-numbers/
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        carry = 0
        current = root
        while l1 or l2 or carry != 0:
            addition = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
            carry = addition // 10
            current.next = ListNode(addition % 10)
            current = current.next
            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
        return root.next