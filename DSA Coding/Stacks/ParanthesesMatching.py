
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
    def isEmpty(self):
        if len(self.data) == 0:
            return 1
        return 0
    
s = input()
c = 0
stack=Stack(len(s))
for i in range(len(s)):
    if s[i] == '(' or s[i] == '{' or s[i] == '[':
        stack.push(s[i])
    else:
        if s[i] == ')':
            if stack.pop() != '(':
                print(i+1)
                c = 1
                break
        if s[i] == '}':
            if stack.pop() != '{':
                print(i+1)
                c = 1
                break
        if s[i] == ']':
            if stack.pop() != '[':
                print(i+1)
                c = 1
                break
if stack.isEmpty() == 0 and c != 1:
    c = 1
    print(len(s)+1)
if c == 0:
    print(0)
  



