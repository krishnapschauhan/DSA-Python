# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        # Edge case: only 1 node → delete it and return None
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        # Find middle
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        prev.next = slow.next

        return head
