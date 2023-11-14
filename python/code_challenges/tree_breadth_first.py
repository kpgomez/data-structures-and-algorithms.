from data_structures.binary_tree import BinaryTree


def breadth_first(tree):
    # initialize empty list
    tree_nodes = []  # will contain list of node values
    if tree.root is None:
        return tree_nodes
    tree_queue = [tree.root]  # will hold list of nodes
    # tree_queue.append(tree.root)
    while tree_queue:
        current_node = tree_queue[0]
        tree_nodes.append(current_node.value)
        tree_queue.pop(0)
        if current_node.left:
            tree_queue.append(current_node.left)
        if current_node.right:
            tree_queue.append(current_node.right)
    return tree_nodes
