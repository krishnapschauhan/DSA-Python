"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        prev=None
        curr=head
        
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        return prev
        