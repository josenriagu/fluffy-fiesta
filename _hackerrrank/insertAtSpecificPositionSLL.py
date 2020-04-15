# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# arbitrary Node class, defined already in hackerrank


class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        pass


def insertNodeAtPosition(head, data, position):
    # initialize a new_node with gigven data
    new_node = SinglyLinkedListNode(data)

    # edge case: if position is 0
    if position == 0:
        # then assign new_node's next to head and return new_node
        new_node.next = head
        return new_node

    # initialize current node and current position
    cur_node = head
    cur_pos = 0

    # loop, till we get to one less than the position
    while cur_pos != position - 1:
        cur_node = cur_node.next
        cur_pos += 1

    # save the next value of the current node to a temp variable
    temp = cur_node.next
    # assign new_node to current node's next
    cur_node.next = new_node
    # then assign next value of new_node to the temp variable
    new_node.next = temp

    # return head node
    return head
