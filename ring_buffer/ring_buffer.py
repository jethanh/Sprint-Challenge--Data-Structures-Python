class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity #list of null values up to capacity
        self.length = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        self.current %= self.capacity #when current = capacity, current % capacity = 0, replaces 0th index.
        if self.length < self.capacity: #if length is less than capacity, length increments
            self.length += 1

    def get(self):
        return self.storage[:self.length] #get the full list, by length.


        #[a, b, c, d, e]