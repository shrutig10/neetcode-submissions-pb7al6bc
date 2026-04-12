class RandomizedSet:

    def __init__(self):
        # o(1) insert/remove --> set works best
        # getrandom --> array works best --> convert hashmap to an array and get the index value
        # values can only be inserted once
        self.rnd_set = set()
        

    def insert(self, val: int) -> bool:
        if val in self.rnd_set:
            return False
        self.rnd_set.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.rnd_set:
            return False
        self.rnd_set.remove(val)
        return True
        

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.rnd_set) - 1)
        return list(self.rnd_set)[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()