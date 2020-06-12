class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity 
        self.length = 0

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        self.length += 1
        self.current %= self.capacity #when current = capacity, current % capacity = 0, sets current to 0, item replaces 0th index.
        

    def get(self):
        print(self.storage[:self.length]) #No None values returned, although they are present in the buffer
        return self.storage[:self.length] #get the full list, by length.