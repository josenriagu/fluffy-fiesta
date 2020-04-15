# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

# arbitrary Node class, defined already in hackerrank


class DoublyLinkedListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        pass


def sortedInsert(head, data):
    # initialize a new_node with given data
    new_node = DoublyLinkedListNode(data)

    # edge case: if head is NULL - empty list
    if head == None:
        return new_node

    # edge case: if data is less that head,
    if new_node.data < head.data:
        # set new_node's prev to None
        new_node.prev = None
        # then assign new_node's next to head,
        new_node.next = head
        # and assign head's prev to new_node
        head.prev = new_node
        # and return new_node
        return new_node

    # initialize current node and variable to indicate when position is found
    cur_node = head
    found = False

    # loop,
    while not found:
        # Tail case: data is less than data and next is None,
        if cur_node.data < data and cur_node.next == None:
            # toggle found
            found = True
            # break out of loop
            break
        # if the cur_node's data is greater than or equal data; we have found where to insert
        if cur_node.data >= data:
            # reassign the cur_node to its prev
            cur_node = cur_node.prev
            # toggle found
            found = True
            # break out of loop
            break
        # if both conditions fail, well, assign the cur_node to its next
        cur_node = cur_node.next

    # save the next value of the current node to a temp variable
    temp = cur_node.next
    # assign new_node to current node's next
    cur_node.next = new_node
    # then assign cur_node to new node's prev
    new_node.prev = cur_node
    # finally, assign the temp variable to new node's next
    new_node.next = temp

    # return head node
    return head
