class SimpleQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        return self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def is_empty(self):
        return len(self.__queue) == 0

