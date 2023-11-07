class Node:
    """
    A Node knows its value, left, and right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    A BinaryTree is a non-linear data structure that contains a root/parent node that can point to one or more child nodes
    """

    def __init__(self):
        self.root = None

    # https://www.udemy.com/course/data-structures-algorithms-python/
    def pre_order(self) -> list:
        """
        This is a type of depth first traversal and the order of this traversal is root, left, right
        :return: list a values
        """
        results = []

        def traverse(current: Node):
            if current is None:
                return

            results.append(current.value)

            if current.left is not None:
                traverse(current.left)

            if current.right is not None:
                traverse(current.right)

        traverse(self.root)

        return results

    def in_order(self) -> list:
        """
        This is a type of depth first traversal and the order of this traversal is left, root, right
        :return:
        """
        results = []

        def traverse(current: Node):
            if current is None:
                return

            # check left
            if current.left is not None:
                traverse(current.left)

            # check root
            results.append(current.value)

            # check right
            if current.right is not None:
                traverse(current.right)

        traverse(self.root)

        return results

    def post_order(self) -> list:

        """
        This is a type of depth first traversal and the order of this traversal is left, right, root
        :return:
        """
        results = []

        def traverse(current: Node):
            if current is None:
                return

            if current.left is not None:
                traverse(current.left)

            if current.right is not None:
                traverse(current.right)

            results.append(current.value)

        traverse(self.root)

        return results
