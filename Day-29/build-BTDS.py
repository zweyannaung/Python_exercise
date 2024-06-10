class Node:
    def __init__(self, myData):
        self.data = myData
        self.left = None
        self.right = None


def insert_data(new_data, node):
    if node is None:
        root: Node = Node(new_data)
        return root

    if new_data < node.data:
        node.left = insert_data(new_data, node.left)

    else:
        node.right = insert_data(new_data, node.right)

    return node


if __name__ == '__main__':
    root_node = Node(15)
    root_node = insert_data(10, root_node)
    print(root_node.data)