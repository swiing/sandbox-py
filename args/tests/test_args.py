import unittest

from src import args

class ArgsTest(unittest.TestCase):

    def setUp(self):
        self.sample = args.AClass(1,2,3,ka="a",kb="b")

    def test_repr(self):
        self.assertEqual(repr(self.sample),
                         repr({"args":(1,2,3),"ka": "a","kb": "b"}))
