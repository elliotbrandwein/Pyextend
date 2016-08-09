# does not exist in python 2.7+
from collections.abc import Mapping,MutableSequence


def extend(*args):
    # for testing purposes only
    def func():
        pass
    if args:
        target = args[0]
    else:
        target = {}
    i = 1
    args_length = len(args)
    deep = False
    options = None
    # Handle a deep copy situation
    if isinstance(target, bool):
        if target:
            deep = target

            # Skip the boolean and the target
            if i < args_length:
                target = args[i]
            else:
                target = {}
            i += 1

        # this will simulate how jquery handles false, it will only not
        # replicate it if the only arg is false, jquery would return the extend
        # function itself, this will just pass a blank dict
        else:
            if i < args_length:
                return args[i]
            else:
                return {}
# Handle case when target is a string or something (possible in deep copy)
    if not isinstance(target, Mapping) and not isinstance(target, type(func)) \
            and not isinstance(target, MutableSequence):
        print("sees a non-dict/list")
        target = {}

    for index in range(i, args_length):
        # only deal with non-None values
        if args[index] is not None:
            options = args[index]
            if isinstance(options, Mapping):
                # print("options:", options)
                for name in options:
                    if target and name in target:
                        src = target[name]
                    else:
                        src = None
                    if options and name in options:
                        copy = options[name]
                    else:
                        copy = None
                    # Prevent never-ending loop
                    if target == copy:
                        continue

                    copy_is_list = isinstance(copy, MutableSequence)
                    # Recurse if we're merging dicts or lists
                    if deep and copy and (isinstance(copy, Mapping) or copy_is_list):

                        if copy_is_list:
                            if src is not None and isinstance(src, MutableSequence):
                                clone = src
                            else:
                                clone = []
                        else:
                            if src is not None and isinstance(src, Mapping):
                                clone = src
                            else:
                                clone = {}

                        # never move original objects, clone them
                        if not isinstance(name, Mapping):
                            target[name] = extend(deep, clone, copy)
                        else:
                            for deep_name in name:
                                name = deep_name
                            if name in target:
                                target[name] = extend(deep, clone, copy)

                    # Don't bring in undefined values
                    elif copy is not None and target:
                        target[name] = copy
            else:
                print("options", options)
                print("target", target)
                return options

    # handles the missing last layer on a deep copy,
    if len(target) == 0 and options:
        target = options

    return target

# TODO merging true with lists

# bug 1
# sample_dict1 = {"red": [ {"foo": 1, "bling": 1}, "value", "more",["value"] ] }
# sample_dict2 = {"red": [{"foo": 2, "bar": 1}, "hi"]}
# sample_dict3 = {"red": [{"foo": 2, "bar": 1, "bling": 1}, "hi", "more"]}
# print("sample1:", sample_dict1)
# print("sample2:", sample_dict2)
# print("extend:", extend(True, sample_dict1, sample_dict2))
# print("correct v:", sample_dict3 )