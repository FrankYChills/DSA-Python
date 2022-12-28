class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index):
        if index > self.size - 1:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.next.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        newnode = Node(val)
        newnode.next = curr.next
        curr.next = newnode
        self.size += 1

    def deleteAtIndex(self, index, val):
        # imp - >= self.size cause there will be no node at self.size
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1
