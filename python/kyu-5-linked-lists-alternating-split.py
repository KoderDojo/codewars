class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def add(head, data):
    if head is None:
        return Node(data)

    current_node = head
    while current_node.next is not None:
        current_node = current_node.next

    current_node.next = Node(data)

    return head


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('head cannot be none')

    first = None
    second = None

    current_node = head
    i = 0

    while current_node is not None:
        if i % 2 == 0:
            first = add(first, current_node.data)
        else:
            second = add(second, current_node.data)

        i += 1
        current_node = current_node.next

    return Context(first, second)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

c = alternating_split(n1)

node = c.first
while node is not None:
    print(node.data)
    node = node.next

print('-----')
node = c.second
while node is not None:
    print(node.data)
    node = node.next

