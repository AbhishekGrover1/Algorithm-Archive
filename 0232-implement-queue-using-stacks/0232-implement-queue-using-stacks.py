class MyQueue(object):

    def __init__(self):
        self.in_stack = []   # Used for push operations
        self.out_stack = []  # Used for pop/peek operations

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :type x: int
        :rtype: int
        """
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack

    def _transfer(self):
        # Transfer elements from in_stack to out_stack only when out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())