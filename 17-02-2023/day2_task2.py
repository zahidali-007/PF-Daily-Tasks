class LifoQueue:
    def __init__(self):         # __init__: This method initializes the queue as an empty list
        self.queue = []

    def push(self, item):        #push: This method adds an item to the beginning of the queue using list concatenation
        self.queue = [item] + self.queue


    #pop: This method removes the last item from the queue using the pop method of the list, which removes and returns the last element of the list

    def pop(self):  
        if self.is_empty():
            return None
        item = self.queue[0]
        self.queue = self.queue[1:]
        return item

    def is_empty(self):         # is_empty: This method returns True if the queue is empty and False otherwise
        return len(self.queue) == 0


# Here's an example usage of the LifoQueue class

queue = LifoQueue()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())  # Output: 3
print(queue.pop())  # Output: 2
print(queue.pop())  # Output: 1
print(queue.pop())  # Output: None
