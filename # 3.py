
directory = []
students = []
with open("studentInfoText.txt", "r") as file:  # Opens file
    for i in file:
        line = tuple(map(str, i.strip().split(",")))
        # Splits each line of the file into individual tuples as they do not need to be/ should not be edited
        directory.append(line)  # Appends each tuple in the list directory

'''
The nested while loops below ask the user for each item they may be looking for (first name, last name, grade, house, 
and adviser) and adds these values to a dictionary. It then checks for each individual value in each tuple within 
"directory". If the item appears in a tuple, the tuple is added to the list "students". After checking how many 
criteria the user inputted (0-5 items) the program outputs whichever tuples appear in the list "students" as many times 
as criteria that the user has inputted.
'''

while True:
    user_inputs = {}  # Dictionary to hold user inputs

    while True:  # Runs until user inputs valid first name
        f_name = input("First name: ").capitalize()  # Capitalizes input to suit format of tuples
        if f_name.isalpha() or len(f_name) == 0:  # If input only contains letters or nothing was inputted, runs below
            user_inputs['FirstName'] = f_name  # Sets key 'FistName' to equal user's inputted first name
            break
        else:
            print("Input a valid first name.")  # If it does not suit above conditions, will run through loop again

    while True:  # Runs until user inputs valid last name
        l_name = input("Last name: ").capitalize()  # Capitalizes input to suit format of tuples
        if l_name.isalpha() or len(l_name) == 0:  # If input only contains letters or nothing was inputted, runs below
            user_inputs['LastName'] = l_name  # Sets key 'LastName' to equal user's inputted last name
            break
        else:
            print("Input a valid last name.")  # If it does not suit above conditions, will run through loop again

    while True:  # Runs until user inputs valid grade
        grade = input("Grade: ")
        if grade.isnumeric() or len(grade) == 0:  # If input only contains numbers or nothing was inputted, runs below
            user_inputs['Grade'] = grade  # Sets key 'Grade' to equal user's inputted grade
            break
        else:
            print("Input a valid grade.")  # If it does not suit above conditions, will run through loop again

    while True:  # Runs until user inputs valid first name
        house = input("House: ").capitalize()  # Capitalizes input to suit format of tuples
        if house.isalpha() or len(house) == 0:  # If input only contains letters or nothing was inputted, runs below
            user_inputs['House'] = house  # Sets key 'House' to equal user's inputted house
            break
        else:
            print("Input a valid house.")  # If it does not suit above conditions, will run through loop again

    while True:  # Runs until user inputs valid first name
        adviser = input("Adviser: ").capitalize()  # Capitalizes input to suit format of tuples
        if adviser.isalpha() or len(adviser) == 0:  # If input only contains letters or nothing was inputted, runs below
            user_inputs['Adviser'] = adviser  # Sets key 'Adviser' to equal user's inputted adviser
            break
        else:
            print("Input a valid adviser.")  # If it does not suit above conditions, will run through loop again

    inputted = 0
    for x in user_inputs.values():
        if x != '':  # Checks each user inputted value
            inputted = inputted + 1  # If they inputted anything other than a blank space, inputted is increased by 1

'''The nested for loop below runs through all user inputs, and checks if each tuple contains each input. If the tuple does
contain the input at the correct index, then the tuple is added to the list "students".'''
    for i in range(0, len(user_inputs.values())):  # Runs in the range of the amount of values inputted
        for j in range(0, len(directory)):  # Runs in the range of length of directory containing each line of file
            matched = False
            if directory[j][i] == list(user_inputs.values())[i]:
                # Checks if each directory tuple contains inputted value at correct index, if so then returns True
                matched = True
            if matched:
                students.append(directory[j])  # If True, appends tuple to list "students"
    if inputted > 0:  # If user has inputted any information
        holder = 0
        print("People who fit your inputted criteria:")
        for k in directory:  # Checks each tuple in directory
            if students.count(k) == inputted:
                # If tuple appears in "students" the same amount of times as criteria inputted, prints tuple
                holder = 1
                print(k)
        if holder == 0: # If nothing fits criteria above and nothing is printed, prints statement below
            print("Nobody in the file matches that criteria. ")
    else:
        print("Nobody in the file matches that criteria. ")  # If user has inputted no information, prints statement

    break
