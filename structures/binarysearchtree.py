from enum import Enum


class Traversal(Enum):

    INORDER = 1
    POSTORDER = 2
    PREORDER = 3


class BSTNode:

    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value = None):
        new = BSTNode(value)
        current = self

        while current != None:
            # if greater than or equal current
            if value >= current.value:
                # insert if no right
                if current.right is None:
                    current.right = new
                    return current.right
                # or traverse
                else:
                    current = current.right
            
            # if less than current
            elif value < current.value:
                # insert if no left
                if current.left is None:
                    current.left = new
                    return current.left
                # or traverse
                else:
                    current = current.left

        raise Exception(f'unable to insert value {value} into BST :shrug_emoji:')


    def delete(self, value = None, current = False):
        # find the value in the tree and remove it, shifting the child elements
        # to accomodate for a missing parent

        # if no children, just remove the node
        # if 1 child, put the child where the removed node was
        # if 2 children, get leftmost child (greatest value) and put it where the node is being deleted

        if current is None:
            return False

        if current is False:
            current = self

        raise Exception('deleting is currently not supported')


    def search(self, value = None, current = False):
        # find the value in the tree, or return False
        if current is None:
            return False
        
        # default to head if current is not set
        if current is False:
            current = self

        # this is the leaf you are looking for
        if value == current.value:
            return current

        # traverse left
        if current.left is not None and value < current.value:
            return self.search(value, current.left)
        
        # traverse right
        if current.right is not None and value >= current.value:
            return self.search(value, current.right)
        
        # no left or right node
        raise Exception(f'unable to find value {value} in BST :shrug_emoji:')


    def min(self, current = None):
        # find the lowest value in the tree
        if current is None:
            current = self

        while current.left:
            current = current.left

        return current.value


    def max(self, current = None):
        # find the highest value in the tree
        if current is None:
            current = self
        
        while current.right:
            current = current.right

        return current.value


    def traverse(self, traversal = Traversal.INORDER, current = None):
        # traverse the tree using the provided type
        if current is None:
            return

        if traversal is Traversal.INORDER:
            self.traverse(traversal, current.left)
            print(current.value)
            self.traverse(traversal, current.right)
        elif traversal is Traversal.PREORDER:
            print(current.value)
            self.traverse(traversal, current.left)
            self.traverse(traversal, current.right)
        elif traversal is Traversal.POSTORDER:
            self.traverse(traversal, current.left)
            self.traverse(traversal, current.right)
            print(current.value)

        
if __name__ == "__main__":
    head = BSTNode(15)
    head.insert(7)
    head.insert(22)
    head.insert(9)
    head.insert(8)
    head.insert(11)
    head.insert(16)

    # will throw an exception if fails
    head.search(8)

    print(f'minimum is 7 {head.min() == 7}')
    print(f'maxmimum is 22 {head.max() == 22}')

    head.traverse(Traversal.INORDER, head)
    head.traverse(Traversal.PREORDER, head)
    head.traverse(Traversal.POSTORDER, head)

