class Node:
    """
    A Node class that knows about its value and next
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack():
    """
    A Stack class consists of Nodes that knows only about their top
    """
    def __init__(self):
        # initialization here
        pass

    def push(self, value: str):
        """
        Instance method that adds input value to current stack
        :param value: takes a string as an input representing the value to be pushed onto the stack
        :return: no return
        """
        # method body here
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass
