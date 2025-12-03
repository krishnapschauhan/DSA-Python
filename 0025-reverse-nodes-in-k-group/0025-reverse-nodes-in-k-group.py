# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or k <= 1:
            return head

        # dummy to simplify edge handling
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # fewer than k nodes remain
                    return dummy.next

            group_next = kth.next  # node after the k-group

            # reverse the k nodes
            prev, curr = group_next, group_prev.next
            # after this loop, prev will point to kth (new head of reversed group)
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # connect reversed group back to list
            tail = group_prev.next  # old head is now tail
            group_prev.next = prev
            group_prev = tail  # move group_prev to tail for next iteration
