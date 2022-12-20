# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack:
    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val):
        if not self.min_arr:
            self.min_arr.append(val)
            self.arr.append(val)
            return
        self.arr.append(val)
        if self.min_arr[-1] >= val:
            self.min_arr.append(val)

    def pop(self):
        # only if value at top of main arr is same as val at top in min stack
        if self.min_arr[-1] == self.arr[-1]:
            self.arr.pop()
            self.min_arr.pop()
            return
        # otherwise just pop from the main stack
        self.arr.pop()

    def top(self):
        return self.arr[-1]

    def getMin(self):
        return self.min_arr[-1]
