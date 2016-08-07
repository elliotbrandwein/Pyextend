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
    if not isinstance(target, dict) and not isinstance(target, type(func)) \
            and not isinstance(target, list):
        print("sees a non-dict/list")
        target = {}

    for index in range(i, args_length):
        # only deal with non-None values
        if args[index] is not None:
            options = args[index]
            for name in options:
                if name in target:
                    src = target[name]

                copy = options[name]

                # Prevent never-ending loop
                if target == copy:
                    continue

                copy_is_list = isinstance(copy, list)
                # Recurse if we're merging dicts or lists
                if deep and copy and (isinstance(copy, dict) or copy_is_list ):

                    if copy_is_list:
                        copy_is_list = False
                        if src is not None and isinstance(src, list):
                            clone = src
                        else:
                            clone = []
                    else:
                        if src is not None and isinstance(src, dict):
                            clone = src
                        else:
                            clone = {}

                    # never move original objects, clone them
                    target[name] = extend(deep, clone, copy)

                # Don't bring in undefined values
                elif copy is not None:
                    target[name] = copy

    return target

# TODO fix the true/false part in first param, as well as the merging of dicts, by adding in new dicts
x = {"apple": 0, "banana": {"weight": 52, "price": 100}, "cherry": 97}
y = {"banana": {"price": 200}, "durrian": 100}
z = {"test": 0, "buddy": 4, "hi": 4}
print(extend(True,x, y))
print(extend(x,y))


