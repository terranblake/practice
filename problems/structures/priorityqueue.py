class PriorityQueue:
    
    def __init__(self, student, size = 5):
        self.size = size
        self.student = student
        self.items = []
        
    
    def enqueue(self, value):
        num = len(self.items)
        
        if num == 0:
            self.items = [value]
            return
            
        if self.items[0] >= value and num == self.size:
            return
        
        for x in range(num):
            current = self.items[x]
            
            if current >= value:
                self.items.insert(x, value)
                break
            elif value > current and x == num - 1:
                self.items.append(value)
                break
        
        if len(self.items) > self.size:
            del self.items[0]