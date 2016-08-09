# doesn't exist in python 2.7+
from collections.abc import Mapping, MutableSequence


# for testing purposes only
def func():
    pass


def extend(*arguments):
    if arguments:
        target = arguments
    else:
        target = {}
    i = 1
    args_length = len(arguments)
    deep = False

    # Handle deep copy sitch
    if isinstance(target,bool):
        deep = target
    # Skip the boolean and the target
        if i < args_length:
            target = arguments[i]
        else:
            target = {}
        i += 1

    # Handle case when target is a primitive datatype ( possible in deep copy)
    if not isinstance(target, Mapping) and not isinstance(target, type(func)) \
            and not isinstance(target,MutableSequence):
        target = {}

    # this was coppised to handle only one input, delete later
    if i == args_length:
        target = {}
        i -= 1

    for index in range(i, args_length):

        # only deals with non-none values
        if index < args_length and arguments[index] is not None:
            options = arguments[index]
            for name in options:

                # had to change to fix errors being thrown
                # src = target[name]
                # copy = options[name]
                if target and name in target:
                    src = target[name]
                else:
                    src = None
                if options:
                    copy = options[name]
                else:
                    copy = None

                # Prevent a never-ending loop
                if target == copy:
                    continue
                # recurse if we're merging dicts or arrays
                if deep and copy and (isinstance(copy,MutableSequence) or \
                                      isinstance(copy, Mapping)):
                    if isinstance(copy, MutableSequence):
                        if src and isinstance(src, MutableSequence):
                            clone = src
                        else:
                            clone = []
                    else:
                        if clone and isinstance(clone, Mapping):
                            clone = src
                        else:
                            clone = {}
                    # Never move original objects, clone them
                    target[name] = extend(deep, clone, copy)

                # Don't bring in None values
                elif copy is not None:
                    target[name] = copy
    return target

# sample_dict1 = {"layer1": {"layer2": {"layer3": 1}, "layer2_extra1": 1},
#                 "layer1_extra1": 1}
# sample_dict2 = {"layer1": {"layer2": {"layer3": 2}, "layer2_extra2": 2},
#                 "layer1_extra2": 2}
# result = {"layer1": {"layer2": {"layer3": 2}, "layer2_extra2": 2,
#                      "layer2_extra1": 1}, "layer1_extra1": 1, "layer1_extra2": 2}
sample_dict1 = {"red": [{"foo": 1,"bling":1}, "value","more"]}
sample_dict2 = {"red":[{"foo": 2, "bar":1}, "hi"]}
result = {"red":[{"foo":2, "bar":1,"bling":1}, "hi","more"]}
print("sample one:", sample_dict1)
print("sample two:", sample_dict2)
print("result from extend: ", extend(True, sample_dict1, sample_dict2))
print("what it should be:", result)
