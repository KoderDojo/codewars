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


def insert_sort(head):
    """
    Sort a linked list using insertion sort.
    Creates a new linked list and adds each
    node in sorted by ascending order.

    :param head: Node, head of the linked list
    :return: Node, head of the sorted linked list
    """

    # if empty linked list or only one
    # node in linked list, do nothin.
    if head is None or head.next is None:
        return head

    new_linked_list = None

    current_node = head

    while current_node is not None:
        new_linked_list = sorted_insert(new_linked_list, current_node.data)
        current_node = current_node.next

    return new_linked_list
