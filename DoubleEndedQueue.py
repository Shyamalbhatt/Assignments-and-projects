'''

    
rear[0] => [ __ , __ , __ ] <= front[-1]
             0    1    2
    

'''

class Deque:
    def __init__(self):
        self.data = []

    def enqueueFront(self, e):
        self.data.append(e)

    def enqueueRear(self, e):
        self.data.insert(0, e)

    def is_empty(self):
        return self._len() == 0

    def dequeueFront(self):
        del self.data[-1]

    def dequeueRear(self):
        del self.data[0]

    def _len(self):
        return len(self.data)

    def Rear(self):
        return self.data[0]

    def Front(self):
        return self.data[-1]

    def show_data(self):
        return self.data

d = Deque()
d.enqueueFront(4)
d.enqueueRear(8)
print(d.show_data())


