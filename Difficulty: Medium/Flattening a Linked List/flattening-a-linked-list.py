'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    
    # merge two sorted bottom-linked lists
    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        
        # choose the smaller element
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
        
        result.next = None       # IMPORTANT: remove next pointer
        return result

    # flatten the list
    def flatten(self, root):
        if root is None or root.next is None:
            return root

        # Flatten the next list
        root.next = self.flatten(root.next)

        # Merge current list with the flattened next list
        root = self.merge(root, root.next)

        return root
