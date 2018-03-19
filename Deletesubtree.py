class Node:
    # with data members .data, .left, and .right
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def deleteTree(node):
    if node is not None:
        deleteTree(node.left)
        deleteTree(node.right)
        node.left = node.right = None