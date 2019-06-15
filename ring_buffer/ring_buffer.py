# FIRST SOLUTION
# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = 0
#         self.storage = [None]*capacity

#     def append(self, item):
#         self.storage[self.current] = item
#         # increment current
#         self.current += 1
#         # check if resets
#         if self.current == self.capacity:
#             self.current = 0

#     def get(self):

#         return [item for item in self.storage if item != None]


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current % self.capacity] = item
        # increment current
        self.current += 1

    def get(self):
        if self.current >= self.capacity:
            return self.storage
        else:
            return self.storage[:self.current]


# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# print(buffer.get())
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())
