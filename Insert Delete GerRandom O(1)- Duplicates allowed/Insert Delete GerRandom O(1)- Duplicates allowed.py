class RandomizedCollection:

    def __init__(self):
        #define list which stores all values
        #define dictionary which stores {key=value inserted to collection : value = set(indexes of values in list)}
        #define index function which increments when a value is inserted and decrements when it is removed
        self.data={}
        self.index=0
        self.data2=[]

    def insert(self, val: int) -> bool:
        #append value to list
        self.data2.append(val)
        #if value is already in list, add it under set it belongs, increment index and return False 
        if val in self.data:
            self.data[val].add(self.index)
            self.index+=1
            return False
        #else create new key and value, increment index and return True
        else:
            self.data[val]=set([self.index])
            self.index+=1
            return True

    def remove(self, val: int) -> bool:
        #if val exists in list, remove one of it's index from set 
        if val in self.data:
            rem=self.data[val].pop()
            #pop(index) runs in O(N-index) since each proceding value is shifted,
            #hence value at end of list is copied to value to be removed, then value at end is popped
            self.data2[rem]= self.data2[-1]
            self.data2.pop()
            self.index-=1
            #if position of new index of shifted value is equal to that of next index, then value has already been deleted 
            if  rem != self.index:
                self.data[self.data2[rem]].add(rem)
                self.data[self.data2[rem]].remove(self.index)
            #if val in dictionary has empty set, it does not exist in list, hence delete from dictionary
            if len(self.data[val]) == 0: 
                del self.data[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        #random value from list
        return (random.choice(self.data2))
