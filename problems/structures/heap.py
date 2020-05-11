from enum import Enum


# class HeapType(Enum):

#     MIN = 1
#     MAX = 2


class Heap:

    def __init__(self, size = 100): # , heap_type = HeapType.MIN
        self.size = size
        self.items = [None for x in range(size)]
        self.last = -1
        # self.heap_type = heap_type


    def insert(self, value = None):
        if self.last == self.size:
            raise Exception('Max heap size reached. Bailing!')

        # set right-most index to new value
        self.last += 1
        self.items[self.last] = value
        self.bubbleup(self.last)


    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    
    def bubbleup(self, index = None):
        parent_position = index // 2
        parent = self.items[parent_position]

        # swap new index if previous is smaller
        if parent > self.items[index]:
            self.swap(index, parent_position)
            self.bubbleup(parent_position)

        
    def bubbledown(self, index):
        left_position = index * 2
        right_position = (index * 2) + 1

        left = self.items[left_position]
        right = self.items[right_position]
        current = self.items[index]

        if left != None and left < current:
            self.swap(left_position, index)
            self.bubbledown(left_position)
        elif right != None and right < current:
            self.swap(right_position, index)
            self.bubbledown(right_position)


    def extractmin(self):
        # get minimum
        minimum = self.items[0]

        if minimum is None:
            return None

        # put right-most element in index 0
        self.items[0] = self.items[self.last]
        self.items[self.last] = None

        # decrement last
        self.last -= 1
        
        # bubble down
        self.bubbledown(0)
        return minimum

        
if __name__ == "__main__":
    hp = Heap()

    hp.insert(12)
    hp.insert(15)
    hp.insert(2)
    hp.insert(4)
    hp.insert(17)

    print(hp.extractmin())
    print(hp.items)

    # print(hp.items)