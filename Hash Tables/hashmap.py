class MyHashMap:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size
    
    # The way that a hash map works is that whenever putting a new element, we define its key and its value, values can be duplicate, but keys can't. 
    # Practically, it works the same way that a hash set works with its keys, but in this case, with each key, we have a linked value with that key. 
    def put(self, key: int, value: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for index, (k, v) in enumerate(bucket):
            if k == key: 
                bucket[index] = (key, value)  # This makes it so the element with an equivalent key has its value changed, since we can't have duplicate keys.
                return
        
        bucket.append((key, value))  # This appends the new element to the bucket pointed to by the hashed key.

    def get(self, key: int) -> int:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for k, v in bucket:
            if k == key:
                return v
        
        return -1  # Key wasn't found.

    def remove(self, key: int) -> None:
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return # Since we've found the key which we want to delete, and so we're done from deletion, we can just return out of the method