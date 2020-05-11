class Queue:

    def __init__(self):
        self.items = []


    def enqueue(self, value = None):
        # put item at the top of the stack
        self.items.insert(0, value)


    def dequeue(self):
        return self.items.pop()


    def size(self):
        return len(self.items)


if __name__ == "__main__":
    que = Queue()
    
    for word in ['this', 'is', 'a', 'basic', 'queue']:
        que.enqueue(word)

    print(f'this {que.dequeue() == "this"}')
    print(f'is {que.dequeue() == "is"}')
    print(f'a {que.dequeue() == "a"}')