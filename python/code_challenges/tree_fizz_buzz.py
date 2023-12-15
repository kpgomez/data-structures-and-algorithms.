# from data_structures.binary_tree import BinaryTree
# from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


class KaryNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class KaryTree:
    def __init__(self, root: KaryNode = None):
        self.root = root

    def breadth_first(self):
        queue = Queue()
        # print('self.root line 18', self.root)
        queue.enqueue(self.root)
        collection = []

        while not queue.is_empty():
            node = queue.dequeue()
            collection.append(str(node.value))

            for child in node.children:
                queue.enqueue(child)
        # print('collection', collection)
        return collection

    def copy(self):
        copy = self.breadth_first() # this is a list
        return copy


def check_fizz_buzz(node):
    if int(node) % 15 == 0:
        return "fizzbuzz"
    elif int(node) % 5 == 0:
        return "fizz"
    elif int(node) % 3 == 0:
        return "buzz"
    else:
        return node


# def fizz_buzz_tree_input_node(k_ary_tree_root: KaryNode) -> KaryNode:
#     tree = KaryTree(k_ary_tree_root)
#     print('fizz_buzz_tree.new_tree line 49', tree)
#     copy = tree.copy()
#     clone = []
#     for node in copy:
#         result = check_fizz_buzz(node)
#         clone.append(result)
#     print('clone', clone)
#     return clone


def fizz_buzz_tree(k_ary_tree: KaryTree) -> KaryNode:
    # print('k_ary_tree', k_ary_tree)
    # copy_tree = KaryTree(k_ary_tree.root).copy()
    # print('copy_tree', copy_tree)
    copy_tree = KaryTree(k_ary_tree.root)

    # traverse the copy and build new tree
    current = copy_tree.root
    print('current', current)
    new_tree_queue = Queue()
    new_tree_queue.enqueue(current)
    fizz_check = []
    #
    # while not new_tree_queue.is_empty():
    #     new_node = new_tree_queue.dequeue()
    #     fizz_check.append(new_node)


    # print('copy_tree', copy_tree)
    # clone = []
    # for node in copy_tree.copy():
    #     result = check_fizz_buzz(node)
    #     clone.append(result)
    # print('clone', clone)
    # fizz_tree = KaryTree(KaryNode(clone[0]))
    return copy_tree
    # return clone


if __name__ == "__main__":
    root = KaryNode(1)
    first_child = KaryNode(2)
    second_child = KaryNode(3)
    root.children = [first_child, second_child]
    tree = KaryTree(root)
    # print('tree line 66', tree)
    # print('root', root)
    # print('root.value', root.value)
    # print('root.children', root.children)
    # for child in root.children:
    #     print('child.value', child.value)
    actual = tree.breadth_first()
    # print('actual line 58', actual)
    new = tree.copy()
    # print('new line 61', new)
    # fizz_buzz_tree_input_node(tree)
    fizzy_tree = fizz_buzz_tree(tree)
    copied_tree = fizzy_tree.copy()

