class MyHashSet:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(0, self.size)]

    def _hash(self, key) -> int:
        return key % self.size
    
    def add(self, key: int) -> None:
        # Convert the key into a hash, if the key already exists in this bucket, then we won't add the item since hash sets cannot have duplicate values
        hash_val = self._hash(key)
        if key not in self.buckets[hash_val]:
            self.buckets[hash_val].append(key)

    def remove(self, key: int) -> None:
        hash_val = self._hash(key)
        # We have to check whether the key exists at all. To do this we check whether the key exists in the list pointed to by the hashed bucket.
        if key in self.buckets[hash_val]:
            self.buckets[hash_val].remove(key)

    def contains(self, key: int) -> bool:
        hash_val = self._hash(key)
        if key in self.buckets[hash_val]:
            return True

        return False        