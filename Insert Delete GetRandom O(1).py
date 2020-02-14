import random
class RandomizedSet:

    def __init__(self):        
        self.data = set()
    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True
    def remove(self, val: int) -> bool:
        try:
            self.data.remove(val)
            return True
        except: 
            return False
    def getRandom(self) -> int:
        return (random.sample(self.data,1)[0])
