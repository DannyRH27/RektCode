class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = [0] * 1000000

    def add(self, key: int) -> None:
        self.values[key] = 1

    def remove(self, key: int) -> None:
        self.values[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.values[key]
