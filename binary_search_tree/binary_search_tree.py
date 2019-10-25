from dll_stack import Stack
from dll_queue import Queue
import sys
import io
sys.path.append('../queue_and_stack')


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

        if self.value is target:
            return True
        # edge cases, no kiddos
        elif not self.right and not self.left:
            return False
        # else if target > node, go right, recursively calling contains
        elif target >= self.value:
            return self.right.contains(target)
        # else if target < node, go left, recursively calling contains
        else:
            return self.left.contains(target)

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
# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

        # Start on the top
        # Go into directions until you can't go
        # Go back until you find the one you can
        # go in a different direction
        # continue until done

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            variable = queue.dequeue()
            print(variable.value)
            if variable.left:
                queue.enqueue(variable.left)
            if variable.right:
                queue.enqueue(variable.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stackAttack = Stack()
        stackAttack.push(node)
        while stackAttack.size > 0:
            variable = stackAttack.pop()
            print(variable.value)
            if variable.left:
                stackAttack.push(variable.left)
            if variable.right:
                stackAttack.push(variable.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
