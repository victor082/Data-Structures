# import sys

# from dll_stack import Stack
# from dll_queue import Queue
# sys.path.append('..\queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):  # we're just using the value, key is value
        self.value = value
        self.left = None
        self.right = None
    # * 'insert' adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.

    def insert(self, value):
        if value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)

    def contains(self, target):
        # *  'contains' searches the binary search tree
        # start from root aand traverse the tree
        # we can stop at the first instance of a value for finding and deleting. Deleting moves up the left or smaller child.
        # we know its not found if we get to a node that doesn't have children
        if self.value is target:
            return True
        elif not self.right and not self.left:
            return False
        elif target >= self.value:
            return self.right.contains(target)

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        pass
