from sys import version_info
from types import FunctionType

PY_33 = version_info >= (3, 3)

if PY_33:
    from collections.abc import Mapping, MutableSequence
else:
    from collections import Mapping, MutableSequence


def extend(*args):
    src = None
    copy = None
    clone = None
    if args:
        target = args[0]
    else:
        target = {}
    args_length = len(args)
    i = 1
    deep = False
    if isinstance(target, bool):
        deep = target

        if args_length > 1:
            target = args[i]
        else:
            target = {}
        i += 1

    # handle if target is not of type Mapping, MutableSequence, or Function
    if not isinstance(target, MutableSequence) and not \
            isinstance(target, Mapping) \
            and not isinstance(target, FunctionType):
        target = {}

    for index in range(i, args_length):
        if index <= args_length:
            options = args[index]
        else:
            options = None

        # Handle if to-be-merged variable is a dict-type
        if isinstance(options, Mapping):
            for name in options:
                if name in target:
                    src = target[name]
                if name in options:
                    copy = options[name]
                if target == copy:
                    continue

                if deep and copy and (isinstance(copy, Mapping)
                                      or isinstance(copy, MutableSequence)):

                    copy_is_list_type = isinstance(copy, MutableSequence)
                    if copy_is_list_type:
                        copy_is_list_type = False
                        if src and isinstance(src, MutableSequence):
                            clone = src
                        else:
                            src = []
                    else:
                        if src and isinstance(src, Mapping):
                            clone = src
                        else:
                            src = {}
                    target[name] = extend(deep, clone, copy)

                else:
                    target[name] = copy

        # Handle if to-be-merged variable is a list-type
        elif isinstance(options, MutableSequence):

            target_length = len(target)
            list_length = len(options)
            # overshoot is for adding a larger list to a smaller
            overshoot = False
            for i in range(0, list_length):
                element = options[i]

                if target_length < i:
                    overshoot = True

                # hack to fix test_true_merge_reg_dict_with_dict_with_list
                if target_length == 0:
                    target = [element]
                    target_length += 1

                elif not isinstance(element, Mapping):
                    if target_length <= i:
                        target.append(element)
                    else:
                        target[i] = element
                elif not overshoot and not isinstance(target[i], Mapping):
                    target[i] = element

                # this will take care of overlapping dicts in two lists
                else:
                    target[i] = extend(deep, target[i], element)

    return target