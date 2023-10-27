from data_structures.queue import Queue


class AnimalShelter:
    """
    AnimalShelter class can only hold dog and cat instances
    """
    def __init__(self):
        self.animals = Queue()

    def enqueue(self, animal):
        self.animals.enqueue(animal)

    def dequeue(self, pref=None) -> str:
        # if pref is None:
        #     return self.dequeue()
        # if pref == 'cat':
        #     # search for cat closest to front of queue
        #
        # if pref == 'dog':
        #     # search for dog closest to front of queue
        #     pass
        if pref == 'dog':
            return self._dequeue_by_preference('dog')
        elif pref == 'cat':
            return self._dequeue_by_preference('cat')
        else:
            if pref is not None:
                return None
            if self.animals.is_empty():
                raise IndexError("No animals available for adoption.")
            return self.animals.dequeue()

    def _dequeue_by_preference(self, pref):
        current = self.animals.front
        prev = None
        while current:
            if current.value.species == pref:
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
