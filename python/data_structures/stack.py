class Node:
    """
    A Node class knows about its value and next
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    A Stack class is made up of Nodes. It only knows about its top
    """
    def __init__(self):
        self.top = None

    def push(self, value: str):
        """
        An instance method of class Stack that adds the input value to current stack
        :param value: takes a string as an input representing the value to be pushed onto the stack
        :return: there is no return
        """
        # step one: create a new node
        new_node = Node(value)
        # step two: assign new_node.next to the same pointer as top
        new_node.next = self.top
        # step three: point top to new_node ** pointing goes in this direction -> **
        self.top = new_node

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass
