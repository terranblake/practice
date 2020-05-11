class Stack:

    def __init__(self):
        self.items = []


    def push(self, value = None):
        # put item at the top of the stack
        self.items.append(value)


    def pop(self):
        return self.items.pop()


    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stk = Stack()
    
    for word in ['this', 'is', 'a', 'basic', 'stack']:
        stk.push(word)

    stk.pop()
    stk.pop()
    stk.pop()

    print(f'stack is size 2 {stk.size() == 2}')