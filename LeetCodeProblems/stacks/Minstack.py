class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = ""

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.min = val
            self.stack.append((val, self.min))
        else:
            self.stack.append((val, self.min))
            if self.min > val:
                self.min = val
            
        

    def pop(self):
        """
        :rtype: None
        """
        x = self.stack.pop()
        if not self.stack:
            self.min = None
        elif x[0] <= self.min:
            self.min = x[1] 
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function."""