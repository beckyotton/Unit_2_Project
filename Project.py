'''
The function below takes in a tuple, and returns the largest and smallest numbers in the tuple. If the tuple has more
than one item, it checks each item in the tuple against each other, adding 1 to the variable bigger and 1 to the
variable smaller every time it is ether bigger or smaller than another number in the tuple. If either of these variables
equals the length of the tuple - 1, this indicates it is the biggest or smallest number and it is then added to another
tuple and returned through this. If there is one item in the tuple, a tuple of this item twice will be returned. If
there are no items, a statement claiming there are no items in the tuple will be returned.
'''

def extremeTuple(args):
    if len(args) > 1:  # If length of tuple above 1
        biggest = 0
        smallest = 0
        for x in range(len(args)):  # Runs for each item in tuple
            bigger = 0
            smaller = 0
            for y in range(0, len(args)):  # Runs for the length of the tuple
                if args[x] > args[y]:  # If tuple item is larger than another number in the tuple, increases bigger by 1
                    bigger = bigger + 1
                if args[x] < args[y]:  # If tuple item is smaller than other number in the tuple, increases smaller by 1
                    smaller = smaller + 1
            if bigger == len(args)-1:  # If bigger = to length of tuple - 1, this number is larger than all others
                biggest = args[x] # Biggest is set to according item in tuple
            elif smaller == len(args)-1:  # If smaller = to length of tuple - 1, this number is smaller than all others
                smallest = args[x]  # Smallest is set to according item in tuple
        tuple_1 = (biggest, smallest)
        return tuple_1  # Returns tuple consisting of smallest and biggest number
    elif len(args) == 1:
        tuple_1 = (args[0], args[0])  # If tuple length is 1, returns a tuple of this number in a tuple twice
        return tuple_1
    else:
        return "That tuple is empty, so there is no maximum or minimum value."  # If tuple length = 0, prints statement


args = (90, 89, 67, 200)
print("Here is the biggest, then smallest number in that tuple:")
print(extremeTuple(args))  # Runs function and prints what it returns
