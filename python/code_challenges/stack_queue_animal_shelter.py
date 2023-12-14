from data_structures.queue import Queue, Node
from data_structures.invalid_operation_error import InvalidOperationError


class Animal(Node):
    def __init__(self, value: str, next = None):
        self.value = value
        self.next = next


class Cat(Animal):
    """
    Node holds the name of the cat or dog object, along with its species, and also knows about the next Node.
    """
    def __init__(self, name: str = None):
        self.name = name
        self.species = "cat"


class Dog(Animal):
    """
    Node holds the name of the cat or dog object, along with its species, and also knows about the next Node.
    """
    def __init__(self, name: str = None):
        self.value = name
        self.species = "dog"


class AnimalShelter(Queue):
    """
    AnimalShelter class is the queue structure that holds the dog and cat instances
    """
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, animal: Animal) -> None:
        # check for empty queue
        if self.front is None:
            new_node = Animal(animal)
            self.front = new_node
            self.rear = new_node
        else:
            # step one: create new node
            new_node = Animal(animal)
            # step two: point rear.next to new_node
            self.rear.next = new_node
            # step three: point rear to new_node
            self.rear = new_node

    def dequeue(self, pref: str = None ) -> Animal:
        # raise Exception when empty
        if self.front is None:
            raise InvalidOperationError

        if pref not in ('dog', 'cat'):
            return None

        while True:
            current = self.front
            # check if pref == species
            if current.value.species == pref:
                # step one: create a ref that points to front
                old_front = self.front
                # step two: point front to front.next
                self.front = old_front.next
                # step three: point old_front.next to None
                old_front.next = None
                # return value of old_front
                return old_front.value
            # move to next node
            else:
                current = self.front
                self.front = current.next


#
# if __name__ == "__main__":
#     georgina = Dog('georgina')
#     print(georgina)
#     print(georgina.value)
#     print(georgina.species)
#     shelter = AnimalShelter()
#     shelter.enqueue(georgina)
#     shelter.dequeue('dog')
    # current = shelter.dequeue(georgina.)

#
# class AnimalShelter:
#     """
#     AnimalShelter class can only hold dog and cat instances
#     """
#     def __init__(self):
#         # this initializes AnimalShelter as a Queue instance
#         self.animals = Queue()
#
#     def enqueue(self, animal: object) -> None:
#         """
#         An instance method that adds the animal to the back of the queue
#         :param animal: an object that represent the species added to the shelter
#         :return: None
#         """
#         # check if Dog or Cat instance
#         if not isinstance(animal, (Cat, Dog)):
#             raise ValueError('Only instances of Cat or Dog allowed')
#         # enqueue if Dog or Cat
#         self.animals.enqueue(animal)
#
#     def dequeue(self, pref=None) -> str:
#         """
#         An instance method that removes the animal from the front of the queue
#         :param pref: a string that represents the species to be removed from the shelter
#         :return: string specifying the specie removed
#         """
#         # check if pref is dog
#         if pref == 'dog':
#             return self._dequeue_by_preference('dog')
#         # check if pref is cat
#         elif pref == 'cat':
#             return self._dequeue_by_preference('cat')
#         # other conditions
#         else:
#             # if pref is neither dog nor cat
#             if pref is not None:
#                 return None
#             # if queue is empty
#             if self.animals.is_empty():
#                 raise IndexError("No animals available for adoption.")
#             # return animal at front of queue
#             return self.animals.dequeue()
#
#     def _dequeue_by_preference(self, pref: str):
#         """
#         An instance method that iterates through the queue starting at the front of the queue
#         and finds the first animal that matches the species/preference
#         :param pref: string representing species to be removed from the shelter
#         :return: string representing animal removed from the queue
#         """
#         # set current to the front of the queue for iteration purposes
#         current = self.animals.front
#         # set ref for previous node
#         prev = None
#         # while current is not None or truthy
#         while current:
#             # checks to see if current node value matches the pref
#             if current.value.species == pref:
#                 # point prev node to next node
#                 if prev:
#                     prev.next = current.next
#                 # point front to next node
#                 else:
#                     self.animals.front = current.next
#                 # point rear node to prev
#                 if not current.next:
#                     self.animals.rear = prev
#                 return current.value
#             prev = current
#             current = current.next
#         raise IndexError(f"No {pref}s available for adoption.")
#
#
#
# class Dog:
#     def __init__(self, name='unknown'):
#         self.name = name
#         self.species = 'dog'
#
#
# class Cat:
#     def __init__(self, name='unknown'):
#         self.name = name
#         self.species = 'cat'
