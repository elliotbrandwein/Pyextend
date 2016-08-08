# doesn't exist in python 2.7.12
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
            print("options: ", options)

            # this will not go inside a list
            if isinstance(options,Mapping):
                for name in options:
                    print("name: ", name)
                    if name in target:
                        print("src= target name: ",target[name])
                        src = target[name]
                    else:
                        print("src=None")
                        src = None
                    #if its a dict we take the value, if its a list we copy it whole
                    if options and isinstance(options, Mapping):
                        print("copy=options[name]:", options[name])
                        copy = options[name]
                    else:
                        # here is where we see the list
                        print("copy=name:", name)
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
                        if name == copy:
                            var = None
                            for x in name:
                                target = extend(deep, clone, copy)
                        else:
                            print("clone: ", clone,"copy: ",copy)
                            target[name] = extend(deep, clone, copy)

                    # Don't bring in undefined values
                    elif copy is not None and target:
                        target[name] = copy
            else:
                for lists in options:
                    for x in range(0,len(lists)):
                        if isinstance(lists[x],Mapping):
                            pass
                            # put code to handle a dict in a list here
                return options

    print("target: ", target)
    return target

# TODO fix the merging with true, for overlapping values, and dicts in lists
sample_dict1 = {"foo": 1}
sample_dict3 = {"here": {"there": 1}}
sample_dict2 = {"bar": {"test":[[1,"2",True],[1,{"here":1},3]]} }
# print(extend(True,sample_dict1,sample_dict3))
# sample_dict1 = {"layer1": {"layer2": {"layer3": {"last_layerer": 1}}}}
# sample_dict2 = {"layer1": {"layer2": {"layer4": {"last_layer": {"one_more": 1}}}}}
# sample_dict3 = {"layer1": {"layer2": {"layer4": {"last_layer": 0}}}}
print(sample_dict1)
print(sample_dict2)
print(extend(sample_dict1, sample_dict2))