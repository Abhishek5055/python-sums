class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self  # Returns itself as the iterator

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += 1
            return result
        raise StopIteration

# Creating an iterable object
my_iterable = MyIterator(1, 5)

# Iterating over the iterable using a for loop
for num in my_iterable:
    print(num)

# Output:
# 1
# 2
# 3
# 4
