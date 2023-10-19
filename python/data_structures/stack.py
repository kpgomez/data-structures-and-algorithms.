from data_structures.invalid_operation_error import InvalidOperationError


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
    def __init__(self, top: Node=None):
        self.top = top

    def push(self, value: str):
        """
        An instance method of class Stack that adds the input value to current stack
        :param value: takes in a string that represents the value to be pushed onto the stack
        :return: None
        """
        # step one: create a new node
        new_node = Node(value)
        # step two: assign new_node.next to the same pointer as top
        new_node.next = self.top
        # step three: point top to new_node ** pointing goes in this direction -> **
        self.top = new_node

    def pop(self) -> str:
        """
        An instance method of class Stack that removes Node from the top of the current stack and reassigns top the previous node's next
        :return: the string representing the value of the Node that was removed
        """
        # raise exception when empty
        if self.top is None:
            # https://chat.openai.com/c/edad9274-75c4-4640-9a55-3a36178ac3f6
            raise InvalidOperationError("Method not allowed on empty collection")
        # create a ref that points to the same node as top
        old_node = self.top
        # point top to current top.next
        self.top = self.top.next
        # remove next from the ref
        old_node.next = None
        return old_node.value

    def peek(self) -> str:
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self) -> bool:
        if self.top is None:
            return True
        # A more pythonic syntax per Jacob's recommendation
        # return self.top is None
