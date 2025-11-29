# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        l1,l2=headA,headB

        while l1!=l2:
            l1=l1.next if l1 else headB
            l2=l2.next if l2 else headA

        return l1
        