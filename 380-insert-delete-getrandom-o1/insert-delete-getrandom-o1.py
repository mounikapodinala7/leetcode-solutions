import random

class RandomizedSet:
    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        lastElement = self.list[-1]
        
        # Swap index with last element
        self.list[index] = lastElement
        self.map[lastElement] = index
        
        # Remove the last element
        self.list.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        randomIndex = random.randint(0, len(self.list) - 1)
        return self.list[randomIndex]