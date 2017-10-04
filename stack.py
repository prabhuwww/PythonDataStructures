# Stack implementation using Python
import logging


class Stack(object):

    def __init__(self):
        # Create an empty stack
        logging.info('Created an empty stack')
        self.__stack = []

    def push(self, item):
        """ Pushes an item into the stack """
        self.__stack.append(item)
        logging.info('%s Inserted to stack', item)

    def pop(self):
        """Remove the last item in the stack"""
        if len(self.__stack) > 0:
            logging.info('Pop element from stack')
            return self.__stack.pop()
        else:
            return

    def peek(self):
        """Return the value of the last item in the list"""
        logging.info('Peeking - top most item on the stack')
        if len(self.__stack) > 0:
            return self.__stack[-1]
        else:
            return

    def is_empty(self):
        """Checks if stack is empty"""
        logging.info('Is empty?')
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def size(self):
        """Return the size of the stack"""
        logging.info('Returning size:')
        return len(self.__stack)