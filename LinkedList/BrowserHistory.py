class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage):
        self.head = Node(homepage)
        self.curr = self.head
        self.size = 1

    def visit(self, url):
        newNode = Node(url)
        self.curr.next = newNode
        newNode.prev = self.curr
        self.curr = newNode
        newNode.next = None

    def back(self, steps):
        for _ in range(steps):
            if not self.curr.prev:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self,steps):
        for _ in range(steps):
            if not self.curr.next:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val