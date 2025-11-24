# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr=head

        while curr:
            while curr.next and curr.next.val==curr.val:
                curr.next=curr.next.next
            curr=curr.next
        return head 