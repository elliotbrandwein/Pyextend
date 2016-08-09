import unittest

from extend import extend


class TestExtend(unittest.TestCase):
    def test_0_dicts(self):
        print("testing extend with no input")
        self.assertEqual(extend(), {})
        print("test: passed")

    def test_1_dict(self):
        print("\n" + "testing extend with one dict")
        sample_dict = {"test": 1}
        self.assertEqual(extend(sample_dict), sample_dict)

    def test_1_list(self):
        print("\n"+"testing extend with one list")
        sample_list = ["value",1,2.0,False,None]
        self.assertEqual(extend(sample_list),sample_list)

    def test_2_dicts(self):
        print("\n" + "testing extend with two dicts")
        sample_dict1 = {"foo": 1}
        sample_dict2 = {"bar": 2}
        result = {"foo": 1, "bar": 2}
        self.assertEqual(extend(sample_dict1, sample_dict2), result)

    def test_false_extend_with_2_params(self):
        print("\n" + "testing extend of two dicts with false")
        sample_dict1 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2 = {"banana": {"price": 200}, "durian": 100}
        self.assertEqual(extend(False, sample_dict1, sample_dict2),
                         sample_dict1)

    def test_false_with_1_param(self):
        sample_dict1 = {"banana": {"price": 200}, "durian": 100}
        self.assertEqual(extend(False, sample_dict1), sample_dict1)

    def test_false_with_0_params(self):
        print("\n"+"testing extend with only false as arg")
        self.assertEqual(extend(False), {})

    def test_true_extend(self):
        print("\n" + "testing a extend of two dicts with true")
        sample_dict1 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2 = {"banana": {"price": 200}, "durian": 100}
        result = {"apple": 0, "banana": {"weight": 52, "price": 200},
                        "cherry": 97, "durian": 100}
        self.assertEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_recursive_dicts(self):
        print("\n" + "testing merging of a recursive dicts")
        sample_dict1 = {"foobar": 1}
        sample_dict2 = {"layer1": {"layer2": {"layer3": {"last_layer": 0}}}}
        result = {"foobar": 1, "layer1":
            {"layer2": {"layer3": {"last_layer": 0}}}}
        self.assertEqual(extend(sample_dict1, sample_dict2), result)

    def test_merge_on_deep_layer(self):
        print("\n" + "testing merging on a deep layer")
        sample_dict1 = {"layer1": {"layer2": {"layer3": {"last_layer": 1}}}}
        sample_dict2 = {"layer1": {"layer2": {"layer_3": {"last_layer": 2}}}}
        result = {"layer1": {"layer2": {"layer_3": {"last_layer": 2}}}}
        self.assertEqual(extend(sample_dict1, sample_dict2), result)

    def test_one_merging_list_with_primitive_datatypes(self):
        print("\n" + "testing merging a list into a dict")
        sample_dict1 = {"foo": 1, "bar": 1}
        sample_dict2 = {"bar": [1, "2", 3.0, True, None], "foobar": 1}
        result = {"foo": 1, "bar": [1, "2", 3.0, True, None],
                        "foobar": 1}
        self.assertEqual(extend(sample_dict1, sample_dict2), result)

    def test_true_merge_with_lists_no_overlapping_dicts(self):
        print("\n" + "testing merging dicts with lists that don't overlap")
        sample_dict1 = {
            "outer": [{"foo": 1, "bar": 1}, "extra1", "extra2", ["extra3"]]}
        sample_dict2 = {"outer": ["more_extra", {"foo": 2, "bar": 2}]}
        result = {
                "outer": ["more_extra", {"foo": 2, "bar": 2},
                          "extra2", ["extra3"]]}
        self.assertEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_true_merge_deep_dicts(self):
        print("\n"+"testing the merging of dicts with deep layers")
        sample_dict1 = {"layer1": {"layer2": {"layer3": {"layer4":
                                                {"layer5": {"layer6": 1}}}}}}
        sample_dict2 = {"layer1": {"layer2": {"layer_other_3": {"layer4":
                                           {"layer5": {"layer6": 1}}}}}}

        result = {'layer1': {
            'layer2': {'layer_other_3': {'layer4': {'layer5': {'layer6': 1}}},
                       'layer3': {'layer4': {'layer5': {'layer6': 1}}}}}}
        self.assertEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_true_merge_with_overlap(self):
        sample_dict1 = {"layer1": {"layer2": {"layer3": 1}, "layer2_extra1": 1},
                        "layer1_extra1": 1}
        sample_dict2 = {"layer1": {"layer2": {"layer3": 2}, "layer2_extra2": 2},
                        "layer1_extra2": 2}
        result = {"layer1": {"layer2": {"layer3": 2}, "layer2_extra2": 2,
                                   "layer2_extra1": 1}, "layer1_extra1": 1,
                        "layer1_extra2": 2}
        self.assertEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_merge_dict_in_list_with_overlap(self):
        sample_dict1 = [{"foo":1, "bling": 1}, "extra1",["extra2"]]
        sample_dict2 = [{"foo":2, "bar": 2}]
        result = [{"foo":2,"bar":2, "bling": 1},"extra1",["extra2"]]
        self.assertEqual(extend(sample_dict1,sample_dict2),result)
if __name__ == '__main__':
    unittest.main()
