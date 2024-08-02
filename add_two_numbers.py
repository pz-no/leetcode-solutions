"""
Runtime: 45ms, Beats 94.95%
Memory: 16.56MB, Beats 67.44%
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail_node = None
        l3 = current_node = ListNode(0, None)

        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current_node.val = carry % 10
            carry = carry // 10
            if tail_node:
                tail_node.next = current_node
            tail_node = current_node
            current_node = ListNode(0, None)

        tail_node.next = ListNode(carry, None) if carry else None

        return l3
