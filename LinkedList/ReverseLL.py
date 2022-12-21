class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        # by default node.next will be None


class Solution:
    def reverseList(self, head):
        if not head:
            return None
        if head and not head.next:
            return head
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# reverseList([1, 2, 3, 4, 5]) --->  1->2->3->4->5
# after passing to reverseList ----> 5->4->3->2->1
