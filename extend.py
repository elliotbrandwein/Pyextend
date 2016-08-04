# for testing purposes only
def func():
    pass

# make it so if no args are passed it will return an empty dict and if there was
# only one dict passed it will return that dict.


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
    for x in range(i, args_length):

        # only deal with non-None values
        if args[x] is not None:
            options = args[x]
            for name in options:
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
                            src = []
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
x = {"hi": 1, "buddy": [{"wow": 4}]}
y = {"buddy": 3}
z = {"test": 0, "buddy": 4, "hi": 4}
print(extend(z, x))



