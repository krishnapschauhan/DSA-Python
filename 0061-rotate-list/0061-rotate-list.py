class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Make circular
        tail.next = head

        # Find new tail (length - k - 1 steps)
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
