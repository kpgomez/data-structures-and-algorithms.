from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self.table = [None]*size

    def set(self, key: str, value: int) -> None:
        """
        This method hashes the key, and sets the key and value pair in the table, handling collisions as needed.
        If the given key already exist, replace its value from the value argument given to this method.
        :param key:
        :type key: str
        :param value:
        :type value: int
        :return: None
        :rtype: NoneType
        """
        hash_index = self.hash(key)
        self.table[hash_index] = value

    def get(self, key: str) -> int:
        """

        :param key:
        :type key:
        :return:
        :rtype:
        """

        return self.table[self.hash(key)]

    def has(self, key: str) -> bool:
        pass

    def keys(self) -> list[str]:
        pass

    def hash(self, key: str) -> int:
        """
        A method that first converts the key into a numerical value by multiplying the ASCII value of each character in the key
        then modulo the product by size of hash table to find the hash index
        :param key:
        :type key:
        :return:
        :rtype:
        """
        product = 1
        for char in key:
            product *= ord(char)

        return product % self.size

