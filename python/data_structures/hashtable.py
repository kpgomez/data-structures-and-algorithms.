class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024):
        # initialization here
        self.size = size
        self._buckets = [None]*size

    def set(self, key: str, value) -> None:
        """
        This method hashes the key, and sets the key and value pair in the table, handling collisions as needed.
        If the given key already exist, replace its value from the value argument given to this method.
        :param key:
        :type key: str
        :param value:
        :type value: 5
        :return: None
        :rtype: NoneType
        """
        hash_index = self.hash(key)
        self._buckets[hash_index] = [key, value]

    def get(self, key: str) -> int:
        """

        :param key:
        :type key:
        :return:
        :rtype:
        """

        return self._buckets[self.hash(key)][1]

    def has(self, key: str) -> bool:
        return key in self._buckets

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
        hash_value = 0
        prime_multiplier = 31
        for char in key:
            hash_value = (hash_value * prime_multiplier) + ord(char)

        return hash_value % self.size


if __name__ == "__main__":
    # table = Hashtable()
    # table.set("silent", True) # silent and listen have the same hash value
    # table.set("ahmad", 30)
    # table.set("listen", "to me")
    # print(("silent", True) in table._buckets    )
    # print(table._buckets)
    # for item in table._buckets:
    #     if item:
    #         print(item)
    pass
