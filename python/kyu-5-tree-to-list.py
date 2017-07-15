"""
Given root of tree with arbitrary number of
child nodes transform data from tree to list.
Where data from neighbour nodes in tree
located in neighbour position in list.

       1
      / \
     2   3  -> [1,2,3,4,5,6,7]
    /|\   \
   4 5 6   7


"""


from collections import deque


class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes


def tree_to_list(tree_root):
    """
    >>> tree = Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])
    >>> l = tree_to_list(tree)
    >>> assert(l == [1, 2, 3, 3, 4, 5, 7])
    """

    if tree_root is None:
        return []

    queue = deque([tree_root])

    node_list = []

    while len(queue) > 0:
        node = queue.popleft()
        node_list.append(node.data)

        if node.child_nodes is not None:
            for child_node in node.child_nodes:
                queue.append(child_node)

    return node_list
