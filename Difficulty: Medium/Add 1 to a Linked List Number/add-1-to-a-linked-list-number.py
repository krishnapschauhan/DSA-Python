# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Yogi Bot Node contains: data, next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addOne(self, head):
        # Step 1: reverse list
        head = self.reverse(head)

        curr = head
        carry = 1
        prev = None

        # Step 2: add carry
        while curr:
            s = curr.data + carry        #  <-- use data, not val
            curr.data = s % 10
            carry = s // 10

            prev = curr
            curr = curr.next

            if carry == 0:
                break

        # Step 3: leftover carry → add new node
        if carry:
            prev.next = Node(carry)      # <-- Yogi Bot uses Node()

        # Step 4: reverse back to original order
        return self.reverse(head)
