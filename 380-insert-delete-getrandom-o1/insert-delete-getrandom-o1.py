import random
class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.lst.append(val)
        self.idx[val] = len(self.lst) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = self.idx[val]
        self.idx[self.lst[-1]] = i
        self.lst[i] = self.lst[-1]
        self.idx.pop(val)
        self.lst.pop()
        return True
        

    def getRandom(self) -> int:
        element = random.choice(self.lst)
        return element
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()