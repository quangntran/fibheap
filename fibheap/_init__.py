from .node import Node
from .fheap import Fheap
# mergeable-heap operations (make-heap, insert, minimum, extract-min, and union)
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
