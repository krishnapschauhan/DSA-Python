#User function Template for python3
'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def deleteAllOccurOfX(self, head, x):
        if head.next is None and head.data == x:
            return None

        prev = None
        temp = head
        new_head = head

        while temp:
            if temp.data == x:

                # FIX 1: correct the typo temp.nest → temp.next
                if prev:
                    prev.next = temp.next

                if temp.next:
                    temp.next.prev = prev

                # FIX 2: update head if needed
                if temp == new_head:
                    new_head = new_head.next

                # FIX 3: DO NOT move prev to temp (deleted node)
                # prev stays same
                temp = temp.next

            else:
                # FIX 4: move prev only when node NOT deleted
                prev = temp
                temp = temp.next

        # FIX 5: return MUST be outside the loop
        return new_head

                    