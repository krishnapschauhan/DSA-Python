# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(next=head)
        prev,curr=dummy,head

        while curr:
            nxt=curr.next
            if curr.val==val:
                prev.next=nxt
            else:
                prev=curr
            curr=nxt
        return dummy.next

        