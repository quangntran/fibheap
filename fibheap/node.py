class Node:
    """Methods:
    - add_child: add a child to the node
    - remove_child: remove a child to the node
    """

    def __init__(self, key, p=None, left=None, right=None,
                 child=None, mark = None):
        """Create a new node in a heap. Attributes:
        - key: the node's key, a number
        - left, right: the node's adjacent siblings. The node and its siblings
        are doubly linked, so they form a circular loop. If x is an only child,
        it is its own left and right sibling.
        - child: the representative child of the node. To access all the
        children of the node, first access the representative child through
        self.child, then access all the child's siblings through self.left or
        self.right.
        - p: the node's parent
        - degree: the number of the node's children whether the node has lost a
        child since the last time it was made the child of another node. Newly
        created nodes are unmarked. A node becomes unmarked whenever it is made
        the child of another node.
        """
        self.key = key
        self.left = left
        self.right = right
        self.p = p # parent
        self.child = child # to any one of its children
        self.degree = 0
        self.mark = False if not mark else mark

    def add_child(self, x):
        """Add a child to the node. If the node currently has no children, the
        child is made the representative child, otherwise, it is added to the
        right of the representative child.

        This procedure updates the child's parent and mark,
        and the node's degree.
        """
        if not self.child:
            self.child = x
            x.left, x.right = x, x
        else:
            right_to_child = self.child.right
            self.child.right = x
            x.left = self.child
            x.right = right_to_child
            right_to_child.left = x
        x.p = self
        self.degree += 1
        x.mark = False

    def remove_child(self, x):
        """ remove a child from the node's child list. This procedure does not
        update the child's parent and does not allow removing a child that does
        not exist. Updating the child's parent is the reponsibility of routines
        that call this function.
        """
        if not self.child:
            raise ValueError('Child list is currently empty')
        if self.degree == 1: # has 1 child
            self.child = None
        else: # >= 2 children
            if self.child is x:
                self.child = x.right
            left_to_x, right_to_x = x.left, x.right
            left_to_x.right = right_to_x
            right_to_x.left = left_to_x
        self.degree -= 1
