# from data_structures.binary_tree import BinaryTree
# from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class KaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def breadth_first(self):
        queue = Queue()
        # print('self.root line 18', self.root)
        queue.enqueue(self.root)
        collection = []

        # while queue is not empty
        while not queue.is_empty():
            node = queue.dequeue()
            # print('line 25', node.value, node.children)
            collection.append(str(node.value))

            for child in node.children:
                # print('child line 29', child.value)
                queue.enqueue(child)
        # print('collection', collection)
        return collection


def check_fizz_buzz(node):
    # print('fizz buzz node line 40', node)
    # print('node.value line 41', node.value)
    if node.value % 15 == 0:
        return "FizzBuzz"
    elif node.value % 5 == 0:
        return "Buzz"
    elif node.value % 3 == 0:
        return "Fizz"
    else:
        return str(node.value)


def fizz_buzz_tree(k_ary_tree: KaryTree) -> Node:
    # maintain ref to old root
    before_fizz_root = k_ary_tree.root

    # check fizzbuzz on  root node
    fizzed_root = Node(check_fizz_buzz(before_fizz_root))
    # print(fizzed_root)
    # print(fizzed_root.value)

    # # create new fizzed tree
    new_tree = KaryTree(fizzed_root)
    #
    # use queue to traverse old tree
    queue = Queue()
    queue.enqueue(before_fizz_root)

    current = before_fizz_root
    fizz_current = fizzed_root

    collection = []

    while not queue.is_empty():
        node = queue.dequeue()
        collection.append(node)
        for child in node.children:
            queue.enqueue(child)
            # # print('line 73', queue)
            # # print('line 74', collection)
            print(child.value)
            # print('grand children', child.children)
            # print('fizz current.children', fizz_current.children)
            # fizz_current.children.append(Node(check_fizz_buzz(child)) for item in collection)
            fizz_current.children.append(Node(check_fizz_buzz(child)))
                # for grandchild in child.children:
                #     fizz_current.children.append(Node(check_fizz_buzz(grandchild)))

    return new_tree


if __name__ == "__main__":
    root = Node(1)
    first_child = Node(2)
    second_child = Node(3)
    third_child = Node(4)
    fourth_child = Node(5)
    grandchild_one = Node(10)
    grandchild_two = Node(15)
    fourth_child.children = [grandchild_one, grandchild_two]
    root.children = [first_child, second_child, third_child, fourth_child]
    tree = KaryTree(root)
    # print('tree line 109', tree)
    print('tree breadth first line 110', tree.breadth_first())
    fizzy_tree = fizz_buzz_tree(tree)
    print('fizz_tree.bfs line 112', fizzy_tree.breadth_first())
    # print('tree line 66', tree)
    # print('root', root)
    # print('root.value', root.value)
    # print('root.children', root.children)
    # for child in root.children:
    #     print('child.value', child.value)
    # actual = tree.breadth_first()
    # print('actual line 58', actual)
    # new = tree.copy()
    # print('new line 61', new)
    # fizz_buzz_tree_input_node(tree)
    # fizzy_tree = fizz_buzz_tree(tree)
    # copied_tree = fizzy_tree.copy()



# def fizz_buzz_tree(k_ary_tree: KaryTree) -> Node:
#     # print('k_ary_tree', k_ary_tree)
#     # copy_tree = KaryTree(k_ary_tree.root).copy()
#     # print('copy_tree', copy_tree)
#     copy_tree = KaryTree(k_ary_tree.root)
#
#     # traverse the copy and build new tree
#     current = copy_tree.root
#     print('current line 69', current.value)
#     new_tree_queue = Queue()
#     new_tree_queue.enqueue(current)
#     fizz_check = []
#     #
#     # while not new_tree_queue.is_empty():
#     #     new_node = new_tree_queue.dequeue()
#     #     fizz_check.append(new_node)
#
#
#     # print('copy_tree', copy_tree)
#     # clone = []
#     # for node in copy_tree.copy():
#     #     result = check_fizz_buzz(node)
#     #     clone.append(result)
#     # print('clone', clone)
#     # fizz_tree = KaryTree(KaryNode(clone[0]))
#     return copy_tree
#     # return clone


# def fizz_buzz_tree(k_ary_tree: KaryTree) -> Node:
#     new_tree = KaryTree(check_fizz_buzz(k_ary_tree.root))
#     # print('new', new_tree)
#     # print('new value line 67', new_tree.root)
#     # result = check_fizz_buzz(k_ary_tree.root)
#     # print('result', result)
#     # print('type of result', type(result))
#     # k_ary_tree.root.value = result
#     # new_tree = KaryTree(k_ary_tree.root)
#     # print('new tree line 73', new_tree)
#
#     # traverse the copy and build new tree
#     # current = new_tree.root
#     # print('current line 77', current.value)
#     # new_tree_queue = Queue()
#     # new_tree_queue.enqueue(current)
#     fizz_check = []
#     #
#     # while not new_tree_queue.is_empty():
#     #     new_node = new_tree_queue.dequeue()
#     #     fizz_check.append(new_node)
#
#
#     # print('copy_tree', copy_tree)
#     # clone = []
#     # for node in copy_tree.copy():
#     #     result = check_fizz_buzz(node)
#     #     clone.append(result)
#     # print('clone', clone)
#     # fizz_tree = KaryTree(KaryNode(clone[0]))
#     print('new tree', new_tree)
#     return new_tree
#     # return clone



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


# def copy(self):
#     copy = self.breadth_first() # this is a list
#     return copy
