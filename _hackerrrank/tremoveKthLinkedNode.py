# Complete the 'removeKthLinkedListNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def removeKthLinkedListNode(head, k):
    # Write your code here

    # initialize variables
    length = 0  # length of list
    cur_node = head  # head as current node

    # find the length of the list
    # while current node is not None
    while cur_node:
        # increment length
        length += 1
        # move on to the next node
        cur_node = cur_node.next

    # Now that we have found our length
    # edge case: when k is greater than length
    if k > length:
        # don't modify, return head
        return head
    # edge case: when k is equal to length
    if k == length:
        # return the next from head
        return head.next

    # initialize position to be removed, by checking length - k
    pos = length - k
    # initialize head as current node
    cur_node = head
    # initialize temp to hold node before position to be removed
    temp = head
    # initialize next_node to hold node after position to be removed
    next_node = head

    # loop until one step after position to be removed
    for i in range(pos + 1):
        # if iterator count is equal to one less that position,
        if i == pos - 1:
            # assign temp to that node
            temp = cur_node
        # if iterator count is equal to position,
        elif i == pos:
            # assign next_node to its next value
            next_node = cur_node.next
        # move on to the next node
        cur_node = cur_node.next
    # assin temp's next value to next_node, thereby removing the node at position
    temp.next = next_node

    # return head
    return head

# 4/4 test cases