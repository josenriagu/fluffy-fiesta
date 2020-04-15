"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    # if head is None, means list is empty
    if head == None:
        return False
    # initialize current node
    cur_node = head
    # initialize a set to hold visited nodes
    visited = set()
    # while cur node is not None
    while cur_node:
        # add the cur node to visited
        visited.add(cur_node)
        # if the next value is already in visited, a loop is formed
        if cur_node.next in visited:
            return True
        # if nex value is None, tail is reached, no loop is formed
        if cur_node.next == None:
            return False
        # move onto the next node
        cur_node = cur_node.next
