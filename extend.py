from collections.abc import Mapping, MutableSequence


# for testing purposes only
def func():
    pass


def extend(*args):
    if args:
        target = args[0]
    else:
        target = {}
    i = 1
    args_length = len(args)
    deep = False

    # Handle a deep copy situation
    if isinstance(target, bool):
        deep = target

        # Skip the boolean and the target
        if i < args_length:
            target = args[i]
        else:
            target = {}
        i += 1

# Handle case when target is a string or something (possible in deep copy)
    if not isinstance(target, Mapping) and not isinstance(target, type(func)) \
            and not isinstance(target, MutableSequence):
        target = {}

    for index in range(i, args_length):

        # only deal with non-None values
        if args[index] is not None:
            options = args[index]

            for name in options:
                if name in target:
                    src = target[name]
                else:
                    src = None
                # print("name", name, " and options", options)
                if options and isinstance(options,Mapping):
                    copy = options[name]
                else:
                    copy = name
                # Prevent never-ending loop
                if target == copy:
                    continue

                # Recurse if we're or lists or list-type objects
                copy_is_list = isinstance(copy, MutableSequence)
                if deep and copy and (isinstance(copy, Mapping) or copy_is_list):

                    if copy_is_list:
                        copy_is_list = False
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
                    print("new name", name)
                    print("attempted copy", copy)
                    target[name] = extend(deep, clone, copy)

                # Don't bring in undefined values
                elif copy is not None and target:
                    target[name] = copy

    return target

# TODO fix the merging with true
sample_dict1 = {"foo": 1}
sample_dict3 = {"here": {"there": 1} }
sample_dict2 = {"bar": { "layer2": [ {"layer3": [{"layer4": 5}]} ] } }
# print(extend(True,sample_dict1,sample_dict3))
sample_dict1 = {"layer1": {"layer2": {"layer3": {"last_layer": 1}}}}
sample_dict2 = {"layer1": {"layer2": {"layer4": {"last_layer": 0}}}}
sample_dict3 = {"layer1": {"layer2": {"layer4": {"last_layer": 0}}}}
print(extend(True,sample_dict1, sample_dict2))