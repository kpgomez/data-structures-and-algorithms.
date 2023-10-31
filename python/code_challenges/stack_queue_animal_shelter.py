from data_structures.queue import Queue


class AnimalShelter:
    """
    AnimalShelter class can only hold dog and cat instances
    """
    def __init__(self):
        # this initializes AnimalShelter as a Queue instance
        self.animals = Queue()

    def enqueue(self, animal: object) -> None:
        """
        An instance method that adds the animal to the back of the queue
        :param animal: an object that represent the species added to the shelter
        :return: None
        """
        # check if Dog or Cat instance
        if not isinstance(animal, (Cat, Dog)):
            raise ValueError('Only instances of Cat or Dog allowed')
        # enqueue if Dog or Cat
        self.animals.enqueue(animal)

    def dequeue(self, pref=None) -> str:
        """
        An instance method that removes the animal from the front of the queue
        :param pref: a string that represents the species to be removed from the shelter
        :return: string specifying the specie removed
        """
        # check if pref is dog
        if pref == 'dog':
            return self._dequeue_by_preference('dog')
        # check if pref is cat
        elif pref == 'cat':
            return self._dequeue_by_preference('cat')
        # other conditions
        else:
            # if pref is neither dog nor cat
            if pref is not None:
                return None
            # if queue is empty
            if self.animals.is_empty():
                raise IndexError("No animals available for adoption.")
            # return animal at front of queue
            return self.animals.dequeue()

    def _dequeue_by_preference(self, pref: str):
        """
        An instance method that iterates through the queue starting at the front of the queue
        and finds the first animal that matches the species/preference
        :param pref: string representing species to be removed from the shelter
        :return: string representing animal removed from the queue
        """
        # set current to the front of the queue for iteration purposes
        current = self.animals.front
        # set ref for previous node
        prev = None
        # while current is not None or truthy
        while current:
            # checks to see if current node value matches the pref
            if current.value.species == pref:
                # point prev node to next node
                if prev:
                    prev.next = current.next
                # point front to next node
                else:
                    self.animals.front = current.next
                # point rear node to prev
                if not current.next:
                    self.animals.rear = prev
                return current.value
            prev = current
            current = current.next
        raise IndexError(f"No {pref}s available for adoption.")



class Dog:
    def __init__(self, name='unknown'):
        self.name = name
        self.species = 'dog'


class Cat:
    def __init__(self, name='unknown'):
        self.name = name
        self.species = 'cat'
