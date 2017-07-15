class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return '{}'.format(self.data)

"""
If you pass a mutable object into a method, the method
gets a reference to that same object and you can mutate
it to your heart's delight, but if you rebind the reference
in the method, the outer scope will know nothing about it,
and after you're done, the outer reference will still point
at the original object.

http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
"""


def move_node(source, dest):
    if source is None or dest is None:
        raise ValueError('source and dest required.')

    if source.data is None:
        raise ValueError('source must have data.')

    if dest.data is None:
        dest.data = source.data
    else:
        second_node = Node(dest.data)
        second_node.next = dest.next

        dest.data = source.data
        dest.next = second_node

    if source.next is not None:
        source.data = source.next.data
        source.next = source.next.next
    else:
        source.data = None
        source.next = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

source = n1
dest = Node()

move_node(source, dest)
print(source)
print(dest)
