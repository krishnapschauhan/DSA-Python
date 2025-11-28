# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):

        # If list has 0 or 1 node -> it's already sorted
        if not head or not head.next:
            return head

        # ---- Step 1: Find middle using slow & fast ----
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        mid = slow.next
        slow.next = None

        # ---- Step 2: Sort left and right halves ----
        left = self.sortList(head)
        right = self.sortList(mid)

        # ---- Step 3: Merge sorted halves ----
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        # Compare and build the sorted list
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # Attach remaining nodes
        if l1:
            curr.next = l1
        else:
            curr.next = l2

        return dummy.next
