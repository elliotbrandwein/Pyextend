import unittest
from extend import extend

class TestExtend(unittest.TestCase):

    def test_0_dicts(self):
        print("testing extend with no input")
        self.assertEqual(extend(), {})
        print("test 1: passed")

    def test_1_dicts(self):
        print("\n"+"testing extend with one input")
        sample_dict = {"test": 1}
        self.assertEqual(extend(sample_dict), sample_dict)
        print("test 2: passed")

    def test_2_dicts(self):
        print("\n"+"testing extend with two inputs")
        sample_dict1 = {"foo": 1}
        sample_dict2 = {"bar": 2}
        sample_dict3 = {"foo": 1, "bar": 2}
        self.assertEqual(extend(sample_dict1, sample_dict2), sample_dict3)
        print("test3: passed")

    def test_true_extend(self):
        print("\n"+"testing a extend of two dicts with true")
        sample_dict1 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2 = {"banana": {"price": 200}, "durian": 100}
        sample_dict3 = {"apple":0,"banana":{"weight":52,"price":200},"cherry":97,
                        "durian":100}
        self.assertEqual(extend(True,sample_dict1, sample_dict2), sample_dict3)
        print("test4: passed")

    def test_value_of_return(self):
        print("\n"+"testing that the return is equal to the target dict")
        sample_dict1 = {"foo": 1}
        sample_dict2 = {"bar": 2}
        sample_dict3 = {"foo": 1, "bar": 2}
        return_dict = extend(sample_dict1, sample_dict2)
        self.assertEqual(return_dict, sample_dict3)
        print("test5: passed")

# x = {"apple": 0, "banana": {"weight": 52, "price": 3}, "cherry": 97}
# y = {"banana": {"price": {"how": {"many": {"layers": 1} } } }, "durrian": 100}
# z = {"test": 0, "buddy": 4, "hi": 4}
# print(extend(True, x, y))
# print(extend(x ,y))
if __name__ == '__main__':
    unittest.main()