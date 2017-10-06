from stack import Stack
import unittest


class TestStack(unittest.TestCase):
    def test_push(self):
        my_stack = Stack()
        self.assertIsNone(my_stack.push(1))

    def test_pop(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        self.assertEqual(my_stack.pop(), 2)

    def test_peek(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        self.assertEqual(my_stack.peek(), 2)

    def test_is_empty(self):
        my_stack = Stack()
        self.assertTrue(my_stack.is_empty())

    def test_size(self):
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        self.assertEqual(my_stack.size(), 2)

if __name__ == '__main__':
    unittest.main()
