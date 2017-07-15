class Node(object):
    """
    Node class provided by Codewars Kata.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):
    """
    Adds a new Node to the beginning of
    a linked list.

    :param head: Node, beginning of linked list or None
    :param data: any, value to store in linked list
    :return: Node, head of the linked list
    """
    if head is None:
        return Node(data)

    new_node = Node(data)

    new_node.next = head
    head = new_node

    return head


def build_one_two_three():
    """
    Creates a link list containing 1 -> 2 -> 3 -> None

    :return: Node, head of the link list
    """
    head = None

    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    return head

