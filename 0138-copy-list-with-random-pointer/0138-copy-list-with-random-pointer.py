"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        mp = {}
        cur = head
        while cur:
            mp[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            mp[cur].next = mp.get(cur.next)
            mp[cur].random = mp.get(cur.random)
            cur = cur.next

        return mp[head]
