name = 'fibhaha'
def makefheap():
    """make-heap in Cormen et al."""
    heap = Fheap()
    return heap
def fheappush(heap, item):
    """insert in Corment et al."""
    heap.insert(Node(item))
def getfheapmin(heap):
    """minimum in Corment et al."""
    return heap.min.key
def fheappop(heap):
    """extract-min in Corment et al."""
    return heap.extract_min().key
def fheapunion(heap, other):
    """union in Corment et al."""
    heap.union(other)

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
        
class Fheap:
    """ Methods: insert, minimum, extract_min, union, decrease_key, delete"""

    def __init__(self, minimum=None):
        """Create a new, empty heap. Attributes:

        - min: points to the node that contains the minimum key
        - num_nodes: number of nodes currently in the heap
        - num_trees: number of roots in the tree A Fibonacci heap can contain
        many trees of min-ordered heap. The roots of these trees are doubly
        linked and form a circular loop as in the case with siblings. The number
        of trees of a Fibonacci heap is always the number of roots.
        - num_marks: number of marked nodes in the heap
        """
        self.min = minimum
        self.num_nodes = 0
        self.num_trees = 0
        self.num_marks = 0

    def remove_root(self,x):
        """ Remove a root from the list of roots of the heap.

        This only updates the pointers of the remaining roots and the number of
        trees of the heap, but does not update the pointers of the removed root
        or those of its children. Those are the responsibility of the routines
        that call this function
        """
        right_to_x, left_to_x = x.right, x.left
        right_to_x.left = left_to_x
        left_to_x.right = right_to_x
        self.num_trees -= 1

    def add_root(self, x):
        """Add a root to the list of roots of the heap.

        If the heap is currently empty, the added root is the min of the heap
        and is its own left and right roots.
        """
        if self.min == None:
            x.left, x.right = x, x
        else:
            right_to_min = self.min.right
            self.min.right = x
            x.left = self.min
            x.right = right_to_min
            right_to_min.left = x
        self.num_trees += 1

    def insert(self, x):
        """Add a node.

        This simply adds the node as a root of the heap, updates the minimum
        node of the heap if necessary, and updates the number of nodes. For example,

        - Before insertion, one root ((2)), minimum = (2):
                (2)
               /   \
              (3)  (4)

        - After inserting (1), two roots ((1) and (2)), minimum = (1):
                (2)---(1)
               /   \
              (3)  (4)
        """
        if self.min == None:
            self.add_root(x)
            self.min = x
        else:
            self.add_root(x)
            if x.key < self.min.key:
                self.min = x
        self.num_nodes += 1

    def minimum(self):
        """Return the node with the minimum key"""
        return self.min

    def extract_min(self):
        """Remove and return the minimum nodeself.

        This procecures moves each of the minimum node's children to the root
        list, removes the minimum node itself from the root list, and
        "consolidate" (see consolidate) the resulted tree.
        """
        z = self.min
        if z != None:
            x = z.child
            for i in range(z.degree):
                y = x.right
                self.add_root(x)
                x.p = None
                x = y
            if z.mark:
                self.num_marks -= 1
            self.remove_root(z)
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.consolidate()
            self.num_nodes -= 1
        return z

    def consolidate(self):
        """ The goal is to reduce the number of trees in the current heap.

        The procedure is as follows (description by Corment et al.):

        1. Find two roots that have the same degree (the same number of
        children)
        2. Merge the two trees rooted at those two roots by making the root with
        larger key one child of the one with smaller key. This procedure is
        called link (see the documentation for link)
        3. Repeat step 1 and 2 until no two roots in the tree have the same degree

        For example,

        - Before consolidating: 3 roots ((1),(4), and (5)), root (1) and (4)
        have the same degree of 1
            (1)---(4)---(5)
             |     |
            (3)   (6)

        - After consolidating: 2 roots ((1) and (5)), root (1) has degree 2
        while root (5) has degree 0.
            (1)---(5)
           /   \
          (3)  (4)
                |
               (6)
        """
        A = [None] * self.num_nodes
        root = self.min
        counter = self.num_trees
        while counter:
            x = root
            root = root.right
            d = x.degree
            while A[d]:
                y = A[d]
                if x.key > y.key:
                    x,y = y,x
                self.link(y, x)
                A[d] = None
                d += 1
            A[d] = x
            counter -= 1
        self.min = None
        for i in range(len(A)):
            if A[i]:
                if self.min == None:
                    self.min = A[i]
                else:
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def link(self, y, x): # y>x
        """Link y to x.

        This procesure makes y a child of x. Because when a node becomes a child
        of another, it has no mark, so the number of marks of the heap is
        updated if necessary.
        """
        self.remove_root(y)
        if y.mark == True:
            self.num_marks -= 1
        x.add_child(y)

    def union(self, other):
        """Make a union of two heaps. This procedure simply concatenates the two
        root lists and updates the minimum node, the number of nodes, the number
        trees, and the number of marks of the heap.
        """
        if not self.min:
            self.min = other.min
        elif other.min:
            self_first_root, other_last_root = self.min.right, other.min.left
            self_first_root.left = other_last_root
            self.min.right = other.min
            other.min.left = self.min
            other_last_root.right = self_first_root

        if (self.min == None) or (other.min != None and other.min.key < self.min.key):
            self.min = other.min
        self.num_nodes += other.num_nodes
        self.num_trees += other.num_trees
        self.num_marks += other.num_marks

    def decrease_key(self, x, k):
        """Decrease node x's key to k.

        k must be larger than the current key of x. If by decreasing x's key to
        k, the heap invariant is violated, x (and therefore along with its
        children) will be cut from its current tree and added to the root list
        (see the function cut). The parent y of x may have had lost one of its
        child before. If this is the case and if y is not a root, then y is, in
        turn, cut from its parent. The nodes are continually cut using
        cascading_cut until it "finds either a root or an unmark node" (Cormen
        et al.).
        """
        if k > x.key:
            raise ValueError('new key is greater than current key')
        x.key = k
        y = x.p
        if y and x.key < y.key:
            self.cut(x, y)
            self.cascading_cut(y)
        if x.key < self.min.key:
            self.min = x

    def cut(self, x, y):
        """ Cut x from y and make it a root.

        x's parent is set to None and x's mark and the heap's number of marks
        are updated if necessary.
        """
        if x.mark:
            self.num_marks -= 1
            x.mark = False
        y.remove_child(x)
        self.add_root(x)
        x.p = None

    def cascading_cut(self, y):
        """Cut continually until it finds either a root or an unmarked node."""
        z = y.p
        if z:
            if not y.mark:
                y.mark == True
                self.num_marks += 1
            else:
                self.cut(y, z)
                self.cascading_cut(z)

    def delete(self, x):
        """Remove x from the heap by first setting its key to minus infinity and
        extracting the heap's min.
        """
        class MaskClass:
            def __lt__(self, other):
                return True

            def __gt__(self, other):
                return False

        mask_key = MaskClass() # the key is smaller than any other keys
        self.decrease_key(x, mask_key)
        self.extract_min()
