from enum import Enum


def height(node = None):
    if node is None:
        return 0

    left_height = 0 if node.left is None else height(node.left)
    right_height = 0 if node.right is None else height(node.right)

    return max(left_height, right_height) + 1


class AVLNode:

    def __init__(self, value = None, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class AVLTree:

    def __init__(self):
        self.head = None
        self.size = 0


    def insert(self, value = None):
        new = AVLNode(value)
        current = self.head

        print(f'inserting node with value {value}')

        self.size += 1

        # first node
        if current is None:
            self.head = new
            return

        while current != None:
            # if greater than or equal current
            if value >= current.value:
                # insert if no right
                if current.right is None:
                    new.parent = current
                    current.right = new

                    self.rebalance(new)
                    return
                # or traverse
                else:
                    current = current.right
            
            # if less than current
            elif value < current.value:
                # insert if no left
                if current.left is None:
                    new.parent = current
                    current.left = new
                    
                    self.rebalance(new)
                    return
                # or traverse
                else:
                    current = current.left

        raise Exception(f'unable to insert value {value} into BST :shrug_emoji:')


    def rebalance(self, current = None):
        if current is None:
            return

        is_unbalanced = height(current.left) > 2 + height(current.right)

        while current != None:
            head = self.head

            is_left_branch = True if head.value > current.value else False
            is_left_sub_branch = True if (current) == -2 else False

            root = current.parent
            pivot = current

            # left-left position
            if is_left_branch is True and is_left_sub_branch is True:
                self.right_rotation(root, pivot)
            # left-right position
            elif is_left_branch is True and is_left_sub_branch is False:
                self.left_rotation(root, pivot)
                self.right_rotation(root, current.parent)
            # right-right position
            elif is_left_branch is False and is_left_sub_branch is False:
                self.left_rotation(root, pivot)
            # right-left
            elif is_left_branch is False and is_left_sub_branch is True:
                self.right_rotation(root, pivot)
                self.left_rotation(root, current.parent)

        return head
        
        return self.rebalance(current.parent)


    def left_rotation(self, root: AVLNode, pivot: AVLNode):
        print(f'left rotation')

        heightr = pivot.right
        root.left = heightr
        pivot.right = heightr.left
        pivot.parent = heightr
        heightr.parent = root
        pivot.right.parent = pivot
        heightr.left = pivot


    def right_rotation(self, root: AVLNode, pivot: AVLNode):
        print(f'right rotation')

        root.left = pivot.right
        pivot.right = root
        root.parent = pivot
        root.left.parent = root


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

        
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(30)
    tree.insert(10)
    tree.insert(35)
    tree.insert(5)
    tree.insert(20)
    tree.insert(15)
    tree.insert(25)



