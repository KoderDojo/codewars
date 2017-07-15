class Node(object):
    """
    Node class provided by Codewars Kata.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    """
    Returns the node at index, where
    index >= 0.

    :param node: Node, the start of the linked list
    :param index: int, index >= 0
    :return: Node, the node at index in linked list
    """
    if node is None:
        raise IndexError('index out of range')

    current_index = 0
    current_node = node

    while current_node is not None:
        if index == current_index:
            return current_node

        current_index += 1
        current_node = current_node.next

    # if we get here, the index is greater
    # than the number of nodes in the linked
    # list.
    raise IndexError('index out of range')
