# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def reverse(head):
    # edge case: empty list or list with one item
    if head == None or head.next == None:
        return head

    # initialize variables
    temp = None
    cur_node = head
    # loop, until cur_node becomes None
    while cur_node:
        # assign cur_node's prev to temp
        temp = cur_node.prev
        # swap next and prev
        cur_node.prev = cur_node.next
        cur_node.next = temp
        # move onto the next node, which is now at prev
        cur_node = cur_node.prev
    # when we exit the loop
    # temp will be holding a node who's prev is now None
    # assign that node to new head
    new_head = temp.prev

    # return new head
    return new_head
