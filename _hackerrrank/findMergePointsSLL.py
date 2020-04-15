# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def findMergeNode(head1, head2):
# initialize variables to hold current heads
    cur_node1,cur_node2 = head1,head2
    
    # helper function to get length of lists
    def getLength(head):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length
    
    # get lengths
    len1,len2 = getLength(head1),getLength(head2)
    
    # move cur_nodes for each list by difference between length
    if len1 > len2:
        for _ in range(len1-len2):
            # using _ instead of i to loop, since we have no direct use for the variable
            cur_node1 = cur_node1.next
    elif len2 > len1:
        for _ in range(len2-len1):
            cur_node2 = cur_node2.next
    
    # At this point, we have current_nodes of both lists at same length\

    # loop while both current_nodes are not equal
    while cur_node2 != cur_node1:
        # move one node ahead for both lists
        cur_node2 = cur_node2.next
        cur_node1 = cur_node1.next
    
    # when it exits the loop, return the data in either of the cur_nodes
    return cur_node1.data
