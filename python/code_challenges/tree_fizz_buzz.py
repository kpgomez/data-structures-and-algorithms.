from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(root):
    k_ary_tree = KaryTree(Node(root))
    print(k_ary_tree.breadth_first())
    node_values = k_ary_tree.breadth_first()
    print(node_values)
    fb_tree = []
    for node in node_values:
        result = check_fizz_buzz(node)
        fb_tree.append(result)
    return fb_tree


def check_fizz_buzz(node):
    if node % 5 == 0 and node % 3 == 0:
        node.value = "FizzBuzz"
    elif node.value % 5 == 0:
        node.value = "Buzz"
    elif node.value % 3 == 0:
        node.value = "Fizz"
    else:
        old_value = node.value
        node.value = str(old_value)
    return node.value
