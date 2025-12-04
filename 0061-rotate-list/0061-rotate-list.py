class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        # 1) Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2) Normalize k
        k %= length
        if k == 0:
            return head

        # 3) Make circular
        tail.next = head

        # 4) Find new tail
        steps = length - k - 1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        # 5) Break circle
        new_head = new_tail.next
        new_tail.next = None
        return new_head
