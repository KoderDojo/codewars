class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(listA, listB):
    """
    Add the linked lists together to form
    one linked list. If both are None,
    return None. If either is None, return
    the other one.

    If both have nodes, this function will
    append listB to listA and return the
    head of listA.

    :param listA: Node, head of linked list
    :param listB: Node, head of linked list
    :return: Node or None, head of combined
        list or None if both lists are None
    """

    # if both lists are None, return None
    if listA is None and listB is None:
        return None

    # if either list is None, return the other
    if listA is None or listB is None:
        return listA if listB is None else listB

    # at this point both lists have nodes.
    # let's loop through listA until we get to the
    # last node and append listB to it.

    current_node = listA

    # find the last node in listA
    while current_node.next is not None:
        current_node = current_node.next

    # append listB to the last node of listA
    current_node.next = listB

    # return the combined linked lists
    return listA
