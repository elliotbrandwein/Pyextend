import unittest
from extend import extend

class TestExtend(unittest.TestCase):

    def test_blank(self):
        print("testing extend with no input")
        self.assertEqual(extend(), {})
        print("test 1: passed")

    def test_one_dict(self):
        print("\n"+"testing extend with one input")
        sample_dict = {"test": 1}
        self.assertEqual(extend(sample_dict), sample_dict)
        print("test 2: passed")

# x = {"apple": 0, "banana": {"weight": 52, "price": 3}, "cherry": 97}
# y = {"banana": {"price": {"how": {"many": {"layers": 1} } } }, "durrian": 100}
# z = {"test": 0, "buddy": 4, "hi": 4}
# print(extend(True, x, y))
# print(extend(x ,y))
if __name__ == '__main__':
    unittest.main()