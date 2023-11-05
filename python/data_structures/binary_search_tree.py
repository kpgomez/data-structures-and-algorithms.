from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    The BinarySearchTree extends the BinaryTree class but with extra properties and a defined organizational structure
    where the value in the left child node is less than its root and the value in the right child node is greater than
    its root
    """

    def __init__(self):
        # initialization here
        self.root = None

    def add(self, value) -> None:
        # method body here
        if self.root is None:
            self.root = Node(value)

        current = self.root

        while current:
            if value == current.value:
                return
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    current = current.left
            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                else:
                    current = current.right

    def contains(self, value) -> bool:
        pass

