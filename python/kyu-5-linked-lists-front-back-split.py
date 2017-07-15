class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}'.format(self.data)


def find_length(head):
    if head is None:
        return 0

    return 1 + find_length(head.next)


def add(head, data):
    if head.data is None:
        head.data = data
        return

    current_node = head
    while current_node.next is not None:
        current_node = current_node.next

    current_node.next = Node(data)


def front_back_split(source, front, back):
    if source is None or source.next is None:
        raise ValueError('source must contain 2 nodes')

    length = find_length(source)

    current_node = source

    for i in range(int(float(length) / 2 + .5)):
        add(front, current_node.data)
        current_node = current_node.next

    while current_node is not None:
        add(back, current_node.data)
        current_node = current_node.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
#n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)

n1.next = n2
n2.next = n3
#n3.next = n4
#n4.next = n5
#n5.next = n6

front = Node()
back = Node()

c = front_back_split(n1, front, back)

node = front
while node is not None:
    print(node.data, node.next.data if node.next is not None else 'None')
    node = node.next

print('-----')
node = back
while node is not None:
    print(node.data)
    node = node.next