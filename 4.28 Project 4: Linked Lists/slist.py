class SList:
    class SListNode:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self._head = None
        self._size = 0

    def insert(self, value):
        new_node = self.SListNode(value)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            previous = None
            while current and current.value.number() < value.number():
                previous = current
                current = current.next
    
            if previous:
                previous.next = new_node
            else:
                self._head = new_node
            new_node.next = current
        self._size += 1



    def find(self, value):
        current = self._head
        while current and current.value != value:
            current = current.next
        return current.value if current else None

    def remove(self, value):
        current = self._head
        previous = None
        while current and current.value != value:
            previous = current
            current = current.next

        if not current:
            return False

        if previous:
            previous.next = current.next
        else:
            self._head = current.next
        self._size -= 1
        return True

    def remove_all(self, value):
        while self.remove(value):
            pass

    def __str__(self):
        result = []
        current = self._head
        while current:
            result.append(str(current.value))
            current = current.next
        return "[" + ", ".join(result) + "]"

    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current:
            value = self._current.value
            self._current = self._current.next
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Invalid index.")

        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def __len__(self):
        return self._size
