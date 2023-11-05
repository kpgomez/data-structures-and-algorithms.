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
        """
        Adds a new node to the BST but only if the value does not already exist in BST
        :param value: any datatype as long as the BST contains the same datatype and datatype can be compared using
        comparison operators <, >, <=, >=, or ==
        :return: None
        """
        if self.root is None:
            self.root = Node(value)

        # for iteration
        current = self.root

        while current:
            # ensures there are no nodes with duplicate values
            if value == current.value:
                return

            # moves left if value is less than current
            if value < current.value:
                # if left is empty, add new node
                if current.left is None:
                    current.left = Node(value)

                # if left is not empty, keep moving down the tree
                else:
                    current = current.left

            # moves right if value is greater than current
            if value > current.value:
                # if right is empty
                if current.right is None:
                    current.right = Node(value)

                # keep moving right if not empty
                else:
                    current = current.right

    # https://chat.openai.com/c/d424e9c6-65ec-47c3-b4fd-05532dfdc8a9
    def contains(self, value) -> bool:
        """
        Traverses the entire BST and checks if any of the nodes contains a specified value
        :param value:
        :return: True if BST contains specified value, False if BST does not contain specified value
        """
        # for traversing the nodes
        current = self.root

        while current:
            # check if specified value is equal to current node's value
            if value == current.value:
                return True
            # move left if specified value is less than current node's value
            if value < current.value:
                if current.left is None:
                    return False
                # move pointer
                else:
                    current = current.left
            # move right is specified value is greater than current node's value
            if value > current.value:
                if current.right is None:
                    return False
                # move pointer
                else:
                    current = current.right
        # all nodes have been checked
        return False

