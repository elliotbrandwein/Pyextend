import unittest

from extend import extend


class TestExtend(unittest.TestCase):
    def test_0_dicts(self):
        self.assertDictEqual(extend(), {})

    def test_1_dict(self):
        sample_dict1 = {"test": 1}
        sample_dict1_untouched = {"test": 1}
        self.assertDictEqual(extend(sample_dict1), sample_dict1_untouched)

    def test_1_list(self):
        sample_list = ["value", 1, 2.0, False, None]
        sample_list_untouched = ["value", 1, 2.0, False, None]
        self.assertListEqual(extend(sample_list), sample_list_untouched)

    def test_2_dicts(self):
        sample_dict1 = {"foo": 1}
        sample_dict2 = {"bar": 2}
        result = {"foo": 1, "bar": 2}
        self.assertDictEqual(extend(sample_dict1, sample_dict2), result)

    def test_true_merge_preserving_originals(self):
        sample_dict1 = {}
        sample_dict2 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2_untouched = sample_dict2
        sample_dict3 = {"banana": {"price": 200}, "durian": 100}
        sample_dict3_untouched = sample_dict3
        result = {"apple": 0, "banana": {"weight": 52, "price": 200},
                  "cherry": 97, "durian": 100}
        self.assertDictEqual(extend(True, sample_dict1, sample_dict2,
                                    sample_dict3), result)
        self.assertDictEqual(sample_dict2, sample_dict2_untouched)
        self.assertDictEqual(sample_dict3, sample_dict3_untouched)

    def test_merge_preserving_originals(self):
        sample_dict1 = {}
        sample_dict2 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2_untouched = sample_dict2
        sample_dict3 = {"banana": {"price": 200}, "durian": 100}
        sample_dict3_untouched = sample_dict3
        result = {"apple": 0, "banana": {"price": 200}, "durian": 100,
                  "cherry": 97}
        self.assertDictEqual(extend(sample_dict1, sample_dict2, sample_dict3),
                             result)
        self.assertDictEqual(sample_dict2, sample_dict2_untouched)
        self.assertDictEqual(sample_dict3, sample_dict3_untouched)

    def test_true_extend(self):
        sample_dict1 = {"apple": 0, "banana": {"weight": 52, "price": 100},
                        "cherry": 97}
        sample_dict2 = {"banana": {"price": 200}, "durian": 100}
        result = {"apple": 0, "banana": {"weight": 52, "price": 200},
                  "cherry": 97, "durian": 100}
        self.assertDictEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_recursive_dicts(self):
        sample_dict1 = {"foobar": 1}
        sample_dict2 = {"layer1": {"layer2": {"layer3": {"last_layer": 0}}}}
        result = {"foobar": 1, "layer1": {"layer2": {"layer3": {"last_layer": 0}
                                                     }}}
        self.assertDictEqual(extend(sample_dict1, sample_dict2), result)

    def test_merge_on_deep_layer(self):
        sample_dict1 = {"layer1": {"layer2": {"layer3": {"last_layer": 1}}}}
        sample_dict2 = {"layer1": {"layer2": {"layer_3": {"last_layer": 2}}}}
        result = {"layer1": {"layer2": {"layer_3": {"last_layer": 2}}}}
        self.assertDictEqual(extend(sample_dict1, sample_dict2), result)

    def test_one_merging_list_with_primitive_data_types(self):
        print("\n" + "testing merging a list into a dict")
        sample_dict1 = {"foo": 1, "bar": 1}
        sample_dict2 = {"bar": [1, "2", 3.0, True, None], "foobar": 1}
        result = {"foo": 1, "bar": [1, "2", 3.0, True, None], "foobar": 1}
        self.assertDictEqual(extend(sample_dict1, sample_dict2), result)

    def test_true_merge_with_lists_no_overlapping_dicts(self):
        sample_dict1 = {
            "outer": [{"foo": 1, "bar": 1}, "extra1", "extra2", ["extra3"]]}
        sample_dict2 = {"outer": ["more_extra", {"foo": 2, "bar": 2}]}
        result = {
                "outer": ["more_extra", {"foo": 2, "bar": 2},
                          "extra2", ["extra3"]]}
        self.assertDictEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_true_merge_reg_dict_with_dict_with_list(self):
        sample_dict1 = {"foo": 1}
        sample_dict1_copy = {"foo": 1}
        sample_dict2 = {"bar": ["list"]}
        sample_dict2_copy = {"bar": ["list"]}
        result = {"foo": 1, "bar": ["list"]}
        self.assertDictEqual(extend(True, sample_dict1, sample_dict2), result)
        self.assertDictEqual(sample_dict2, sample_dict2_copy)

    def test_true_merge_deep_dicts(self):
        sample_dict1 = {"layer1": {"layer2": {"layer3": {"layer4": {"layer5": {
            "layer6": 1}}}}}}
        sample_dict2 = {"layer1": {"layer2": {"layer_other_3": {"layer4": {
            "layer5": {"layer6": 1}}}}}}

        result = {'layer1': {
            'layer2': {'layer_other_3': {'layer4': {'layer5': {'layer6': 1}}},
                       'layer3': {'layer4': {'layer5': {'layer6': 1}}}}}}
        self.assertDictEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_true_merge_with_overlap(self):
        sample_dict1 = {"layer1": {"layer2": {"layer3": 1}, "layer2_extra1": 1},
                        "layer1_extra1": 1}
        sample_dict2 = {"layer1": {"layer2": {"layer3": 2}, "layer2_extra2": 2},
                        "layer1_extra2": 2}
        result = {"layer1": {"layer2": {"layer3": 2}, "layer2_extra2": 2,
                             "layer2_extra1": 1}, "layer1_extra1": 1,
                  "layer1_extra2": 2}
        self.assertDictEqual(extend(True, sample_dict1, sample_dict2), result)

    def test_merge_dict_in_list_with_overlap(self):
        sample_dict1 = [{"foo": 1, "bling": 1}, "extra1", ["extra2"]]
        sample_dict2 = [{"foo": 2, "bar": 2}]
        result = [{"foo": 2, "bar": 2, "bling": 1}, "extra1", ["extra2"]]
        self.assertListEqual(extend(sample_dict1, sample_dict2), result)

    def test_merging_5_things(self):
        sample_dict1 = {"dict1": 1}
        sample_dict2 = {"dict2": 2}
        sample_dict3 = {"dict3": 3}
        sample_dict4 = {"dict4": 4}
        sample_dict5 = {"dict5": 5}
        result = {"dict1": 1, "dict2": 2, "dict3": 3, "dict4": 4, "dict5": 5}
        self.assertDictEqual(extend(sample_dict1, sample_dict2, sample_dict3,
                                    sample_dict4, sample_dict5), result)

    def test_None_is_2nd_arg(self):
        sample_dict1 = {
            "number1": 5, "number2": 7, "string1": "peter",
                          "string2": "pan"}
        sample_dict2 = {"number2": 1, "string2": "x", "new_string": "xxx"}
        sample_dict2_copy = {"number2": 1, "string2": "x", "new_string": "xxx"}
        correct_result = {"number1": 5, "number2": 1, "string1": "peter",
                          "string2": "x", "new_string": "xxx"}
        extend(sample_dict1, None, sample_dict2)
        self.assertDictEqual(sample_dict1, correct_result)
        self.assertDictEqual(sample_dict2, sample_dict2_copy)

    def test_merge_dict_with_Nones(self):
        options = {"number1": 1, "x_string": "x", "string": "new_string"}
        null_dict = {"number1": None}
        correct_result = {"number1": None, "x_string": "x",
                          "string": "new_string"}
        result = extend(options, null_dict)
        self.assertEqual(null_dict["number1"], None)
        self.assertDictEqual(result, correct_result)

    def test_true_merge_with_list_in_dict(self):
        dict_1 = {"apple": [{"price": 100, "wieght": 200}, "extra", "extra"]}
        dict_2 = {"apple": [{"price": 200}, "two", "three"]}
        result = extend(True, dict_1, dict_2)
        correct_result = {"apple": [{"price": 200, "wieght": 200}, "two",
                                    "three"]}
        self.assertDictEqual(result, correct_result)

    def test_true_merge_with_lists_blank_first(self):
        dict_1 = {"apple": [{"price": 100, "weight": 200}, "extra", "extra"]}
        dict_2 = {"apple": [{"price": 200}, "two", "three"]}
        result = extend(True, {}, dict_1, dict_2)
        correct_result = {"apple": [{"price": 200, "weight": 200}, "two",
                                    "three"]}
        self.assertDictEqual(result, correct_result)

if __name__ == '__main__':
    unittest.main()
