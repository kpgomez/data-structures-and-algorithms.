from data_structures.queue import Queue


class AnimalShelter:
    """
    AnimalShelter class can only hold dog and cat instances
    """
    def __init__(self):
        # this initializes AnimalShelter as a Queue instance, so it now has access to all of its methods/attributes
        self.animals = Queue()

    def enqueue(self, animal: object) -> None:
        """
        An instance method that
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
        An instance method that removes the animal from the queue
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
            return self.animals.dequeue()

    def _dequeue_by_preference(self, pref: str):
        """
        An instance method that iterates through the queue and finds the animal that matches the species/pref and also that
        animal has been in the shelter the longest
        :param pref: string representing species to be removed from the shelter
        :return:
        """
        # set current to the front of the queue for iteration purposes
        current = self.animals.front
        # unsure why previous is None
        prev = None
        # while current is not None or truthy
        while current:
            # checks to see if current node value matches the pref
            if current.value.species == pref:
                # still unsure what prev is used for
                if prev:
                    prev.next = current.next
                else:
                    self.animals.front = current.next
                if not current.next:
                    self.animals.last = prev
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
