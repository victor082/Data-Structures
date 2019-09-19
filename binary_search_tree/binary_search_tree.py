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
        # current node is SELF
        # check if self.value is bigger or smaller than new value - left or right
        # We go left or right, then check if node exists
        # if node does not exist than create a node there
        # if node does exist use recurison, call insert on that node

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # *  'contains' searches the binary search tree
        # start from root aand traverse the tree
        # we can stop at the first instance of a value for finding and deleting. Deleting moves up the left or smaller child.
        # we know its not found if we get to a node that doesn't have children
        # Check if the current value is the target, if so, we're done
        # Otherwise, left or right based on bigger or smaller, and then call contains again

        if self.value == target:
            return True
        if self.target < self.value:
            # go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            # go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    def get_max(self):
        # the max node is farthest to the right
        # base case: if there's no right, then the root is the max.
        if not self.right:
            return self.value
        return self.right.get_max()
        # --- Iterative Version ---
        # max_value  = self.value
        # current = self
        # while current:
        #   max_value = current.value
        #   current = current.right
        # return max_value

    def for_each(self, cb):
        # for each performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value.
        # there is a myriad of ways to perform tree traversal; in this case any of them should work.
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
