class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        # initialization here
        self.head = head

    def insert(self, value):
        # method body here
        if self.head is None:
            self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head

    def includes(self, value):

        current = self.head

        linked_list_values = []

        while current:
            linked_list_values.append(current.value)
            current = current.next

        if value in linked_list_values:
            return True
        else:
            return False

    def __str__(self):
        # method body here
        current = self.head

        if current is None:
            return "NULL"

        linked_list_values = ""

        while current:
            # performs logic
            linked_list_values += f"{{ {current.value} }} -> "
            current = current.next

        return linked_list_values + 'NULL'


class TargetError:
    pass
