class Stack:
    def __init__(self,s):
        self.data = []
        self.size=s
        self.top = -1
    def push(self, element):
        self.data.append(element)
        self.top = self.top + 1
    def pop(self):
        popped_element = None
        if(self.top>-1):
            popped_element = self.data.pop() 
            self.top = self.top - 1
        return popped_element
    def peek(self):
        return self.data[self.top]
    def isEmpty(self):
        if len(self.data) == 0:
            return 1
        return 0
    def isFull(self):
        if len(self.data) == self.size :
            return 1
        else:
            return 0


