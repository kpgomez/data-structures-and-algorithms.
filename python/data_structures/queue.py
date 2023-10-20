from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    """
    A Node only knows about its value and next
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    A Queue consists of Nodes. It knows about its front and rear.
    """
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear
        # Jacob's suggestions with front=None removed from parameters
        # self.front = rear
        # self.rear = rear

    def enqueue(self, value: str):
        """
        Adds a new node containing value to the back of the queue with an O(1) Time complexity
        :param value:
        :return: None
        """
        # check for empty queue
        if self.front is None:
            new_node = Node(value)
            self.front = new_node
            self.rear = new_node
        else:
            # step one: create new node
            new_node = Node(value)
            # step two: point rear.next to new_node
            self.rear.next = new_node
            # step three: point rear to new_node
            self.rear = new_node

        # Jacob's suggestions
        # if queue is empty
        # if self.front is None:
        #     new_node = Node(value)
        #     self.front = new_node
        #     self.back = new_node

        # else:
        #     new_node = Node(value)
        #     new_node = self.back
        #     self.back = new_node

    def dequeue(self) -> str:
        """
        Removes the node from the front of the queue
        :return: string representing the value of the node removed
        """
        # raise Exception when empty
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        # step one: create a ref that points to front
        old_front = self.front
        # step two: point front to front.next
        self.front = old_front.next
        # step three: point old_front.next to None
        old_front.next = None
        # return value of old_front
        return old_front.value

    def peek(self) -> str:
        """
        An instance method of class Queue that shows the value of the Node in front
        :return: a string representing the value in front
        """
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.front.value

    def is_empty(self) -> bool:
        """
        An instance method of class Queue that checks if the queue is empty
        :return: a boolean True when empty and False when not empty
        """
        if self.front is None:
            return True
