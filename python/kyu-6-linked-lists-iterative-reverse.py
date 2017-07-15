class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return f'Node({self.data}, {self.next})'


def reverse(head):
    if head is None or head.next is None:
        return head

    previous_node = None
    current_node = Node(head.data, head.next)

    while True:
        next_node = current_node.next
        current_node.next = previous_node
        if next_node is None:
            head.next = current_node.next
            head.data = current_node.data
            break
        previous_node = current_node
        current_node = next_node


a = Node(4, Node(3, Node(2, Node(1))))
reverse(a)
print(a)
