class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_nth(head, index, data):
    # insert new node at beginning of
    # linked list
    if index == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node

    if head is None:
        raise IndexError('index out of range')

    current_index = 1
    previous_node = head
    current_node = head.next

    while current_node is not None:

        # inserting new node in the middle
        # of the linked list
        if index == current_index:
            new_node = Node(data)
            new_node.next = current_node
            previous_node.next = new_node
            return head

        current_index += 1
        previous_node = current_node
        current_node = current_node.next

    # inserting new node to end of linked list
    if index == current_index:
        current_node = Node(data)
        previous_node.next = current_node
        return head

    # if we get here, the code is attempting
    # to insert the node at an index > the
    # end of the linked list
    raise IndexError('index out of range')
