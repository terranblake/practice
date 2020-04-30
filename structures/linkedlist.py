class Node:

    def __init__(self, value = None, node = None):
        self.value = value
        self.next = node


class LL:

    def __init__(self):
        self.head = None


    def search(self, value = None):
        # find the node with this value, or return None
        current = self.head

        while current != None:
            # base condition
            if current.value == value:
                break

            current = current.next

        return current


    def insert(self, value = None):
        node = Node(value)

        # set the head node
        if self.head is None:
            self.head = node
            return

        # find the last element in the LL
        current = self.head
        while current.next != None:
            current = current.next

        # append the new node to the end
        current.next = node
        pass


    def delete(self, value = None):
        # remove the element with value and return True, or return False
        current = self.head
        while current.next != None:
            # cut out the element by simplying referencing the next element
            if current.next.value == value:
                current.next = current.next.next
                return True

            current = current.next

        return False

    
    def print(self):
        current = self.head
        string = []

        while current != None:
            string.append(current.value)
            current = current.next

        print(' '.join(string))
        


if __name__ == "__main__":
    words = ['linked', 'lists', 'are', 'great']
    llist = LL()

    for word in words:
        llist.insert(word)

    verb = llist.search('are')
    print(f'found verb in linked list => {verb.value}')

    llist.delete('linked')
    llist.insert('!')

    llist.print()