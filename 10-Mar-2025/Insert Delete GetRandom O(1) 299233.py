# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.hashmap = set()

        

    def insert(self, val: int) -> bool:

        if (not val in self.hashmap):
            self.hashmap.add(val)
            return True

        else:
            return False

        
        

    def remove(self, val: int) -> bool:

        if (val in self.hashmap):
            self.hashmap.discard(val)
            return True

        else:
            return False


        

    def getRandom(self) -> int:
        return random.choice(list(self.hashmap))
        



