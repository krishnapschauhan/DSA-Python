# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        len=1
        tail=head
        while tail.next:
            len+=1
            tail=tail.next
        if k % len == 0:
            return head
        k=k % len
        tail.next=head
        move = len - k
        newLastNode=self.findNthNode(head,move)
        head= newLastNode.next
        newLastNode.next=None
        return head

    def findNthNode(self,head,move):
        temp=head
        count=1
        while count < move:
            count +=1
            temp=temp.next 
        return temp