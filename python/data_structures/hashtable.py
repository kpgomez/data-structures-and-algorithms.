from data_structures.linked_list import LinkedList


class Hashtable:
    """
    An abstract data structure to hold key/value pairs in an associative array.
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        # self._buckets = [None]*size # table
        # self._buckets = [None]*size
        self._buckets = [[] for _ in range(size)]

    def set(self, key: str, value) -> None:
        """
        This method hashes the key, and sets the key and value pair in the table, handling collisions as needed.
        If the given key already exist, replace its value from the value argument given to this method.
        :param key: The key of the hashtable instance
        :type key: str
        :param value: The value associated with the key
        :type value: can be str, int, bool
        :return: None
        :rtype: NoneType
        """
        hash_index = self.hash(key)

        # replace value if key already exists
        if key in self._buckets[hash_index]:
            self._buckets[hash_index] = [key, value]

        # check if hash_index is already in use
        elif self._buckets[hash_index]:
            previous_pair = self._buckets[hash_index]
            prev_key, prev_value = previous_pair
            self._buckets[hash_index] = [[prev_key, prev_value]]
            self._buckets[hash_index].append([key, value])

        # if hash_index not used
        else:
            self._buckets[hash_index] = [key, value]

    def get(self, key: str) -> int:
        """
        This method returns the value associated with that key in the table.
        :param key:
        :type key:
        :return:
        :rtype:
        """
        if self.has(key):
            return self._buckets[self.hash(key)][1]
        else:
            return None

    def has(self, key: str) -> bool:
        """

        :param key:
        :type key:
        :return:
        :rtype:
        """
        return key in self.keys()

    def keys(self) -> list[str]:
        """

        :return:
        :rtype:
        """
        all_keys = []
        for key in self._buckets:
            if key:
                all_keys.append(key[0])
        return all_keys

    def hash(self, key: str) -> int:
        """
        A method that first converts the key into a numerical value by multiplying the ASCII value of each
        character in the key then modulo the product by size of hash table to find the hash index
        :param key:
        :type key:
        :return:
        :rtype:
        """
        hash_product = 1
        for char in key:
            hash_product *= ord(char)
        return hash_product % self.size


if __name__ == "__main__":
    table = Hashtable()
    # table.set("silent", True) # silent and listen have the same hash value
    # table.set("ahmad", 30)
    # print('before listen', table._buckets)
    # print(type(table._buckets))
    # table.set("listen", "to me")
    # print('after listen', table._buckets)
    # print(table._buckets[992])
    # # print(("silent", True) in table._buckets)
    # # print(table._buckets)
    # # for item in table._buckets:
    # #     if item:
    # #         print(item)
    table.set("apple", "Used for apple sauce")
    print(table._buckets)
    print(table.get("apple"))

