class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    """
    Insert a new node in the correct
    position in a linked list sorted
    ascending.

    :param head: Node, head of linked list
    :param data: any, data of new Node
    :return: Node, head of linked list
    """

    # if linked list is empty, the
    # new node is the head
    if head is None:
        return Node(data)

    new_node = Node(data)

    # new node <= head.
    # new node becomes the head
    if data <= head.data:
        new_node.next = head
        return new_node

    current_node = head

    while current_node.next is not None:

        # we know the new node > current node
        # we just need to check if the new node
        # comes before the next node, and if so,
        # insert it.
        if data <= current_node.next.data:
            new_node.next = current_node.next
            current_node.next = new_node
            return head

        current_node = current_node.next

    # add node to end of linked list
    current_node.next = new_node

    return head
