import unittest
# from my_util import *
# or
# from my_util import one
# or
# requires python directory to be marked as sources root
from utils.my_util import *
from other_utils.my_other_util import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, one())
        self.assertEqual(1, two())


if __name__ == '__main__':
    unittest.main()
