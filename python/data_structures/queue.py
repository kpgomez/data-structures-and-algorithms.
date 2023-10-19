from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    A Queue consists of Nodes. It knows about its front and rear.
    """

    def __init__(self, back=None):
        self.front = back
        self.back = back

    def enqueue(self, value: str):
        """
        Adds a new node containing value to the back of the queue with an O(1) Time complexity
        :param value:
        :return: None
        """
        # step one: create new node
        # new_node = Node(value)
        # # step two: point new_node to same as back
        # new_node.next = self.back
        # # step three: point back to new node
        # self.back = new_node

        # if queue is empty, lines
        if self.front is None:
            new_node = Node(value)
            self.front = new_node
            self.back = new_node

        else:
            new_node = Node(value)
            new_node = self.back
            self.back = new_node


    def dequeue(self) -> str:
        """
        Removes the node from the front of the queue
        :return: string representing the value of the node removed
        """
        # raise Exception when empty
        if self.front is None:
            raise InvalidOperationError

        # step one: create a ref that points to front
        old_front = self.front
        # step two: point front to front.next
        new_front = self.front.next
        # step three: point new front to None
        # new_front.next = None
        # # return value of old_front
        return old_front.value

    def peek(self):
        pass

    def is_empty(self):
        pass
