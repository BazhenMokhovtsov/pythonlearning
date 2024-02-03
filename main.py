distance_dict = {
    #'distance': 130,
    'speed': 100,
    'time': 1.3,
}

my_distance = {
    'distance': 'asd',
    #'speed': 95,
    'time': 1.6,
}

#A function is created to which the dictionary is passed
#If dict has 'distance' and its value is an integer, print the string...
#Else if dict has 'speed' and 'time' as value, print the string...
#Else print the string...
def route_info(**kwargs):  #A function that gets a different set of arguments.
    if kwargs.get('distance') and isinstance(kwargs.get('distance'), int): #The presence of the Distance key in the dictionary is checked.
        return f"Distance to your destination is {kwargs.get('distance')} km."

    #The presence of the "speed" and "time" key in the dictionary is checked.
    if isinstance(kwargs.get('speed'), int) and isinstance(kwargs.get('time'),int):

        speed = kwargs.get('speed')
        time = kwargs.get('time')
        return f"Distance to your destination is {round(speed * time)} km."

    return f"No distance info is avalible."



print(route_info(**my_distance))