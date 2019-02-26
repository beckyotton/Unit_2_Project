'''
This function takes in the dictionary of flights and destinations, city 1 and city 2, and determines if there is a
one-hop option by going into the values (destinations associated with city 1) of city 1, and checking for each of the
values, when they are keys in the dictionary, if any of their values (associated destinations) are city 2, which would
indicate a one-hop available.
'''
def one_hop(flights, city1, city2):
    for i in flights:  # Checks each key in flights
        if i == city1:  # If the key is the same as city 1, runs if statement
            for j in flights[i]:  # Checks each value for that key
                if city2 in flights[j]:  # If the second city is in these values, returns True as there is a one-hop
                    return True


'''
This code represents the body of the program
'''

flights = {'London': ['Paris', 'Dublin'], 'Paris': ['London', 'Dublin'], 'Dublin':
    ['Berlin', 'Paris', 'London'], 'Berlin': ['Dublin', 'Stockholm'], 'Stockholm': ['Berlin']}
city1 = ''  # Sets city 1 and 2 unequal to eligible cities so that while loop below is not true and runs
city2 = ''
print("Welcome to the Flight Checker to see if a route has a one-hop option.")
while city1 not in ['London', 'Paris', 'Dublin', 'Berlin', 'Stockholm'] or city2 not in \
        ['London', 'Paris', 'Dublin', 'Berlin', 'Stockholm'] or city1 == city2:
    # If city 1 and city 2 not in list of possible cities, while loop continues to run
    city1 = input('Input the city you are departing from (London, Paris, Dublin, Berlin, Stockholm). ').capitalize()
    city2 = input('Input the city you are flying to (London, Paris, Dublin, Berlin, Stockholm). ').capitalize()
    # Capitalizes input so it matched capitalized cities in dictionary
if one_hop(flights, city1, city2):  # Runs above function to check if one-hop is available
    print("There is a one hop available for that route.")  # If true, tells the user a one-hop is available
else:
    print("There is no one hop available for that route.")  # If not true, tells the user no one-hop available
