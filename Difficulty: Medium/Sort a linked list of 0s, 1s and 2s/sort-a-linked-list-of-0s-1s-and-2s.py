'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def segregate(self, head):
        # Base case
        if head is None or head.next is None:
            return head

        # Dummy heads
        zeroHead = Node(-1)
        oneHead = Node(-1)
        twoHead = Node(-1)

        zero = zeroHead
        one = oneHead
        two = twoHead

        temp = head

        # Partition the nodes
        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = temp
            elif temp.data == 1:
                one.next = temp
                one = temp
            else:
                two.next = temp
                two = temp
            temp = temp.next

        # Connect the three lists
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None   # End of final list

        # Return head of new list
        return zeroHead.next
    
    