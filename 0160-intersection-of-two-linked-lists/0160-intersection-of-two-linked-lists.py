# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA = 0
        tempA = headA
        while tempA:
            lenA += 1
            tempA = tempA.next

        lenB = 0
        tempB = headB
        while tempB:
            lenB += 1
            tempB = tempB.next

        if lenA > lenB: # A is longer than B
            for _ in range(lenA-lenB):
                headA = headA.next
        elif lenB > lenA: # B is longer than A
            for _ in range(lenB-lenA):
                headB = headB.next

        
        while headA and headB:
            if headA != headB:
                headA = headA.next
                headB = headB.next
            else:
                return headA

        return None
        