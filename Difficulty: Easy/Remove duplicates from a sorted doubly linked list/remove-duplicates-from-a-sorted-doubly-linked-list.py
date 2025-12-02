'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def removeDuplicates(self, head):
        cur = head 
        
        while cur:
            if cur.prev and cur.prev.data == cur.data:
                if cur.prev == head:
                    cur.prev = None        
                    head = cur           
                else:
                    cur.prev.prev.next = cur     
                    cur.prev = cur.prev.prev     
            
            cur = cur.next  
        
        return head