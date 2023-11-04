class Node:
    """
    A Node class knows its value, left, and right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    # https://www.udemy.com/course/data-structures-algorithms-python/
    def pre_order(self) -> list:
        """
        This is a depth first traversal and the order of traversal is root, left, right
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
        This is a depth first traversal and the order of traversal is left, root, right
        :return:
        """
        results = []

        def traverse(current: Node):
            if current is None:
                return

            if current.left is not None:
                traverse(current.left)

            results.append(current.value)

            if current.right is not None:
                traverse(current.right)

        traverse(self.root)

        return results

    def post_order(self) -> list:

        """
        This is a depth first traversal and the order of traversal is left, right, root
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
