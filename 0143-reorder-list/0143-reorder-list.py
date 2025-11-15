# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        #find middle
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reverse the second half
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        
        #merge two halfs
        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
