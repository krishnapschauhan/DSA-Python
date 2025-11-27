# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        if fast==None:
            return head.next
        
        while fast.next:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next
        return head
        