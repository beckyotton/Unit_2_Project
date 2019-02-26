'''
This function takes in the list of the three past numbers that have been chosen by the user, and depending on the
combination of numbers and probability of the next inputted number, it returns 1 or 2 as the computer's number choice.
'''

def comp_number(past_numbers):
    if len(past_numbers) < 3:  # If past_numbers is shorter than 3 spots (3 rounds haven't been played yet), returns 2
        return '2'
    else:
        if past_numbers == ['1', '2', '1'] or past_numbers == ['1', '1', '2'] or past_numbers == ['2', '1', '1'] or \
                past_numbers == ['1', '1', '1']:
            return '2'  # Returns 2 if probability indicates the user likely chose 2
        elif past_numbers == ['1', '2', '2'] or past_numbers == ['2', '1', '2'] or past_numbers == ['2', '2', '1'] or \
                past_numbers == ['2', '2', '2']:
            return '1'  # Returns 1 if probability indicates the user likely chose 2


'''
This code represents the body of the program, where the scores of the computer and user are kept track of, and user 
inputs their number, and the computer's guess is checked against the user's guess to determine which player gets the 
point.
'''

points = {'Me': 0, 'Computer': 0}  # Dictionary which stores the score of the user and computer
past_numbers = []
while points['Me'] < 30 and points['Computer'] < 30:  # Runs until the user or computer achieve 30 points
    my_number = input("What number are you thinking of? (1 or 2) \n")
    while my_number not in ['1', '2']:  # Will not let user out of loop unless they input 1 or 2
        my_number = input("What number are you thinking of? (1 or 2) \n")
    if my_number == comp_number(past_numbers):  # Runs function comp_number to check if computer guessed user number
        points['Computer'] = points['Computer'] + 1  # Computer receives a point if number is the same as user's
        print("The computer guessed your number!")
    else:
        points['Me'] = points['Me'] + 1  # If computer number is not the user's number, user receives a point
        print("The computer didn't guess your number!")
    print("Your score:", points['Me'], "Computer score:", points['Computer'])  # Displays user and computer scores
    if len(past_numbers) == 3:  # Only begins to delete 1st number in list (3 turns prior) once 3 turns have occurred
        del past_numbers[0]  # Deletes the first value in the list, user number from 3 turns ago
    past_numbers.append(my_number)  # Appends most recent number to end of list
if points['Me'] == 30:
    print("You win!")  # If the user gets 30 points, this statement prints
else:
    print("The computer wins.")  # If the computer gets 30 points, this statement prints
