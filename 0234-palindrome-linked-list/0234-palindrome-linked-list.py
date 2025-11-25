# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp

        left,right=head,prev
        while right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True
        