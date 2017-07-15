class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    if node is None:
        return 0

    return 1 + length(node.next)


def count(node, data):
    if node is None:
        return 0

    if node.data == data:
        return 1 + count(node.next, data)

    return count(node.next, data)
