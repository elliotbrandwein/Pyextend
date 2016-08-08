from collections.abc import Mapping,MutableSequence
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
        print("sees a non-dict/list")
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
                if options:
                    # print(name,options)
                    if not isinstance(name,Mapping):
                        copy = options[name]
                    else:
                        copy = name
                # Prevent never-ending loop
                if target == copy:
                    continue

                copy_is_list = isinstance(copy, MutableSequence)
                # Recurse if we're merging dicts or lists
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
                    print("here is the error name:", name)
                    if not isinstance(name, Mapping):
                        target[name] = extend(deep, clone, copy)
                    else:
                        for deep_name in name:
                            print(deep_name)
                            name = deep_name
                        target[name] = extend(deep, clone, copy)

                # Don't bring in undefined values
                elif copy is not None and target:
                    target[name] = copy

    return target

# TODO fix the merging of lists with true