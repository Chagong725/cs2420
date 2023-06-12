class HashMap:
    def __init__(self, capacity=7):
        self._capacity = capacity
        self._size = 0
        self._buckets = [None] * capacity

    def _hash(self, key):
        r, c = key
        return (r * (r + 1) // 2 + c) % self._capacity

    def _find_bucket(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket:
            for i, item in enumerate(bucket):
                if item[0] == key:
                    return index, i
        else:
            self._buckets[index] = []
        return index, None

    def get(self, key):
        index, pos = self._find_bucket(key)
        if pos is not None:
            return self._buckets[index][pos][1]
        raise KeyError

    def set(self, key, value):
        index, pos = self._find_bucket(key)
        if pos is not None:
            self._buckets[index][pos] = (key, value)
        else:
            self._buckets[index].append((key, value))
            self._size += 1
            if self._size / self._capacity >= 0.8:
                self._rehash()

    def remove(self, key):
        index, pos = self._find_bucket(key)
        if pos is not None:
            del self._buckets[index][pos]
            self._size -= 1

    def clear(self):
        self._buckets = [None] * self._capacity
        self._size = 0

    def capacity(self):
        return self._capacity

    def size(self):
        return self._size

    def keys(self):
        result = []
        for bucket in self._buckets:
            if bucket:
                for item in bucket:
                    result.append(item[0])
        return result

    def _rehash(self):
        old_buckets = self._buckets
        self._capacity = self._capacity * 2 - 1
        self._buckets = [None] * self._capacity
        self._size = 0
        for bucket in old_buckets:
            if bucket:
                for key, value in bucket:
                    self.set(key, value)
