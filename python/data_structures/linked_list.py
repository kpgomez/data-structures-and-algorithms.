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
        """

        """
        if self.head is None:
            self.head = Node(value)
        else:
            old_head = self.head
            self.head = Node(value)
            self.head.next = old_head

    def insert_before(self, value, new_value):
        """
        Adds a new node with the given new value immediately before the first node that has the value specified
        """
        # my code that didn't work
        # again have to start at head node
        # current = self.head
        #
        # new_node = Node(value)

        # find node with matching value
        # point new node to the node to insert before
        # point head node to new node
        # while current.next:
        #     if current.value == value:
        #         new_node.next = current
        #         current = current.next
        # self.head.next = new_node

        # with ChatGPT's help AGAIN
        current = self.head

        new_node = Node(new_value)  # Create a new node with the new_value

        while current.next:
            if current.next.value == value:  # Check the next node's value
                new_node.next = current.next  # Set the next of the new node to the next of the current node
                current.next = new_node  # Update the current node's next to the new node
                break  # Exit the loop after insertion
            current = current.next  # Move to the next node in the list

    def append(self, value):
        """
        Adds a new node with the given value to the end of the list
        """
        # my attempt
        # current = self.head
        # while current:
        #     current = current.next
        # # new_node = Node(value)
        # current.next = Node(value)

        #with help from ChatGPT
        ## step one - instantiate new node
        new_node = Node(value)

        ## step two - make new node the head if this is a new linked list
        if self.head is None:
            self.head = new_node
            return

        ## you have to traverse linked list starting at the head
        current = self.head

        ## looks like my attempt was missing .next
        while current.next:
            current = current.next

        ## change the pointer to now point to new_node
        current.next = new_node


    def includes(self, value):
        """

        """
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
