class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    # handle empty link list or link list
    # with 1 node.
    if head is None or head.next is None:
        return head

    current_node = head
    next_node = head.next

    while next_node is not None:

        # if current and next node have same
        # data, remove next node from list.
        if next_node.data == current_node.data:
            current_node.next = next_node.next
            next_node = current_node.next
            continue

        # if gotten here, nodes do not have the
        # same data. increment them.
        current_node = next_node
        next_node = next_node.next

    return head

