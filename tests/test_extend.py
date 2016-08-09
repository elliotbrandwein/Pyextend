import unittest

from extend import extend


class TestExtend(unittest.TestCase):

    def test_0_dicts(self):
        print("testing extend with no input")
        self.assertEqual(extend(), {})
        print("test: passed")

    def test_1_dict(self):
        print("\n"+"testing extend with one input")
        sample_dict = {"test": 1}
        self.assertEqual(extend(sample_dict), sample_dict)


    def test_2_dicts(self):
        print("\n"+"testing extend with two inputs")
        sample_dict1 = {"foo": 1}
        sample_dict2 = {"bar": 2}
        sample_dict3 = {"foo": 1, "bar": 2}
        self.assertEqual(extend(sample_dict1, sample_dict2), sample_dict3)

    def test_false_extend(self):
        print("\n"+"testing extend of two dicts with false")
        sample_dict1 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2 = {"banana": {"price": 200}, "durian": 100}
        sample_dict3 = {"apple": 0, "banana": {"price": 200}, "cherry": 97,
                        "durian": 100}
        self.assertEqual(extend(False, sample_dict1, sample_dict2), sample_dict3)

    def test_true_extend(self):
        print("\n"+"testing a extend of two dicts with true")
        sample_dict1 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2 = {"banana": {"price": 200}, "durian": 100}
        sample_dict3 = {"apple": 0, "banana": {"weight": 52, "price": 200},
                        "cherry": 97, "durian": 100}
        self.assertEqual(extend(True, sample_dict1, sample_dict2), sample_dict3)

    def test_recursive_dicts(self):
        print("\n"+"testing merging of a recursive dicts")
        sample_dict1 = {"foobar": 1}
        sample_dict2 = {"layer1": {"layer2": {"layer3": {"last_layer": 0}}}}
        sample_dict3 = {"foobar": 1, "layer1":
                        {"layer2": {"layer3": {"last_layer": 0}}}}
        self.assertEqual(extend(sample_dict1, sample_dict2), sample_dict3)

    def test_merge_on_deep_layer(self):
        print("\n"+"testing merging on a deep layer")
        sample_dict1 = {"layer1": {"layer2": {"layer3": {"last_layer": 1}}}}
        sample_dict2 = {"layer1": {"layer2": {"layer4": {"last_layer": 0}}}}
        sample_dict3 = {"layer1": {"layer2": {"layer4": {"last_layer": 0}}}}
        self.assertEqual(extend(sample_dict1, sample_dict2), sample_dict3)

    def test_one_merging_list_with_primitive_datatypes(self):
        print("\n"+"testing merging a list into a dict")
        sample_dict1 = {"foo": 1001, "bar": 1}
        sample_dict2 = {"bar": [1, "2", 3.0, True, None], "foobar": 1}
        sample_dict3 = {"foo": 1001, "bar": [1, "2", 3.0, True, None],
                        "foobar": 1}
        self.assertEqual(extend(sample_dict1, sample_dict2), sample_dict3)


if __name__ == '__main__':
    unittest.main()