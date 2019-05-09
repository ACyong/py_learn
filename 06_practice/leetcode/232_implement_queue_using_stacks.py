# -*- coding: utf-8 -*-


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.pop_stack:
            return self.pop_stack.pop()
        if self.push_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.pop_stack:
            return self.pop_stack[-1]
        if self.push_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not bool(self.push_stack or self.pop_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
#
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
#
# print(param_2, param_3, param_4)
