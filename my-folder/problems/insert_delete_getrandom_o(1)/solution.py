class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        
        if val not in self.hashmap:
            self.array.append(val)
            self.hashmap[val] = len(self.array)-1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        
        if val in self.hashmap:
            index = self.hashmap[val]
            last_element = self.array[-1]
            
            self.hashmap[last_element], self.array[index] = index, self.array[-1]
            
            self.array = self.array[:-1]
            
            del self.hashmap[val]
            
            return True
        
        else:
            return False
        

    def getRandom(self) -> int:
        
        return choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()