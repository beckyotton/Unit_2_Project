from random import *
'''
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
'''
'''
directory = []
students = []
with open("studentInfoText.txt", "r") as file:
    for i in file:
        line = tuple(map(str, i.strip().split(",")))
        directory.append(line)

while True:
    user_inputs = {}

    while True:
        f_name = input("First name: ").capitalize()
        if f_name.isalpha() or len(f_name) == 0:
            user_inputs['FirstName'] = f_name
            break
        else:
            print("Input a valid first name.")

    while True:
        l_name = input("Last name: ").capitalize()
        if l_name.isalpha() or len(l_name) == 0:
            user_inputs['LastName'] = l_name
            break
        else:
            print("Input a valid last name.")

    while True:
        grade = input("Grade: ")
        if grade.isnumeric() or len(grade) == 0:
            user_inputs['Grade'] = grade
            break
        else:
            print("Input a valid grade.")

    while True:
        house = input("House: ").capitalize()
        if house.isalpha() or len(house) == 0:
            user_inputs['House'] = house
            break
        else:
            print("Input a valid house.")

    while True:
        adviser = input("Adviser: ").capitalize()
        if adviser.isalpha() or len(adviser) == 0:
            user_inputs['Adviser'] = adviser
            break
        else:
            print("Input a valid adviser.")

    inputted = 0
    for x in user_inputs.values():
        if x != '':
            inputted = inputted + 1

    for i in range(0, len(user_inputs.values())):
        for j in range(0, len(directory)):
            matched = False
            if directory[j][i] == list(user_inputs.values())[i]:
                matched = True
            if matched:
                students.append(directory[j])
    if inputted > 0:
        holder = 0
        print("People who fit your inputted criteria:")
        for k in directory:
            if students.count(k) == inputted:
                holder = 1
                print(k)
        if holder == 0:
            print("Nobody in the file matches that criteria. ")
    else:
        print("Nobody in the file matches that criteria. ")
    break
    '''


def one_hop(flights, city1, city2):
    for i in flights:
        if i == city1:
            for j in flights[i]:
                if city2 in flights[j]:
                    return True


flights = {'London': ['Paris', 'Dublin'], 'Paris': ['London', 'Dublin'], 'Dublin':
    ['Berlin', 'Paris', 'London'], 'Berlin': ['Dublin', 'Stockholm'], 'Stockholm': ['Berlin']}
city1 = ''
city2 = ''
while city1 != 'London' or city1 != 'Paris':  # Fix to make sure input valid city and don't input same for both
    city1 = input("Input the city you are departing from (London, Paris, Dublin, Berlin, Stockholm). ")
    city2 = input("Input the city you are flying to (London, Paris, Dublin, Berlin, Stockholm). ")
if one_hop(flights, city1, city2):
    print("There is a one hop available for that route.")
else:
    print("There is no one hop available for that route.")

'''
def guess_number():
    my_points = 0
    comp_points = 0
    while my_points < 30 and comp_points < 30:
    number = randint(1, 2)
'''
