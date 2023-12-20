from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue


def check_fizz_buzz(node):
    if node.value % 15 == 0:
        return "FizzBuzz"
    elif node.value % 5 == 0:
        return "Buzz"
    elif node.value % 3 == 0:
        return "Fizz"
    else:
        return str(node.value)


def fizz_buzz_tree(k_ary_tree: KaryTree) -> KaryTree:
    # maintain ref to old root
    before_fizz_root = k_ary_tree.root

    # check fizzbuzz on  root node
    fizzed_root = Node(check_fizz_buzz(before_fizz_root))

    # # create new fizzed tree
    new_tree = KaryTree(fizzed_root)

    # use queue to traverse old tree
    queue = Queue()
    queue.enqueue(before_fizz_root)

    fizz_current = fizzed_root

    while not queue.is_empty():
        node = queue.dequeue()
        for child in node.children:
            queue.enqueue(child)
            fizz_current.children.append(Node(check_fizz_buzz(child)))

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
    fizzy_tree = fizz_buzz_tree(tree)
