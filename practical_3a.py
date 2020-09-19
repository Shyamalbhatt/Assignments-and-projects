class Stack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            print('Stack is Empty')
        return self.data[-1]
    
    def pop(self):
        if self.is_empty():
            print('Stack is Empty')
        return self.data.pop()

s = Stack()
print(s.is_empty())
s.push(5)
s.push(7)
s.push(9)
s.push(6)
s.push(2)
print(s.top())
print(s.__len__())
s.pop()
