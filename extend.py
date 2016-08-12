from sys import version_info
from types import FunctionType

PY_33 = version_info >= (3, 3)

if PY_33:
    from collections.abc import Mapping, MutableSequence
else:
    from collections import Mapping, MutableSequence


def extend(*args):
    options = None
    name  = None
    src = None
    copy = None
    copyIsArray = None
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
    if not isinstance(target, MutableSequence) and not isinstance(target, Mapping) \
        and not isinstance(target, FunctionType):
        target = {}
    for index in range(i,args_length):
        if index <= args_length:
            options = args[index]
        else:
            options = None
        if isinstance(options, Mapping):
            for name in options:
                if name in target:
                    src = target[name]
                if name in options:
                    copy = options[name]
                if target == copy:
                    continue

                if deep and copy and (isinstance(copy, Mapping) \
                                              or isinstance(copy, MutableSequence)):
                    copyIsArray = isinstance(copy, MutableSequence)
                    if copyIsArray:
                        copyIsArray = False
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
                elif copy is not None:
                    target[name] = copy
        elif isinstance(options,MutableSequence):
            target_length = len(target)
            overshoot = False
            for i in range(0, len(options)):
                element = options[i]

                if target_length < i:
                    overshoot = True
                if not isinstance(element, Mapping):
                    target[i] = element
                elif not overshoot and not isinstance(target[i], Mapping):
                    target[i] = element
                # this will take care of overlapping dicts in two lists
                else:
                    target[i] = extend(deep, target[i], element)
            return target
    return target
