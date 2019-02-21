def extremeTuple(args):
    if len(args) > 1:
        biggest = 0
        smallest = 0
        for x in range(len(args)):
            bigger = 0
            smaller = 0
            for y in range(0, len(args)):
                if args[x] > args[y]:
                    bigger = bigger + 1
                if args[x] < args[y]:
                    smaller = smaller + 1
            if bigger == len(args)-1:
                biggest = args[x]
            elif smaller == len(args)-1:
                smallest = args[x]
        tuple_1 = (biggest, smallest)
        return tuple_1
    elif len(args) == 1:
        tuple_1 = (args[0], args[0])
        return tuple_1
    else:
        return "That tuple is empty, so there is no maximum or minimum value."


args = (87, 90, 67)
print(extremeTuple(args))


