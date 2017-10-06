# queue module
import logging


class MyQueue(object):

    def __init__(self):
        logging.info('Created an empty queue')
        self.__queue = []

    def enqueue(self, item):
        """Add an item to the queue"""
        self.__queue.insert(0, item)

    def dequeue(self):
        """Remove the first item in the queue"""
        return self.__queue.pop()

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.__queue) > 0

    def size(self):
        """Check size of queue"""
        return len(self.__queue)
