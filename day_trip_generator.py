import random

destination_list = ["New York City", "Toranto", "Miami", "London", "Paris", "Moscow", "Death Valley", "Detroit", "Las Vagas", "Mexico City"]
restaurant_list = ["McDonalds", "Ramsy's Steakhouse", "Crumble Cookies", "Wendies", "Chick-Fil-A", "Sonic", "Cracker Barrel", "Outback"]
transportation_list = ["Semi-truck", "SUV", "Sports Car", "Boat", "Plane", "Scooter", "Bike", "Train", "Helecopter"]
entertainment_list = ["Rave", "Classical Ball", "Magician", "Inspirational Speaker Convention", "Football Game", "MMA Fight", "Music Concert"]

#Selects and returns a random item from a list
def list_item_randomnizer(selected_list):
    selected_item = random.choice(selected_list)
    return selected_item
#Takes in a one string input from user
def get_user_choice_input():
    return input("Are you satisfied with your choices (yes/no): ")

#Prints the trip list
def print_trip_list(selected_list):
    print(selected_list)

#Prints the final trip list 
def print_final_list(selected_list):
    print(f"You will be going to {selected_list[0]}, eating at {selected_list[1]}, taking a {selected_list[2]}, and attending a {selected_list[3]}!!!")

#Takes in a list finds what needs re-randomnized and returns the re-randomnizes list.
def day_trip_rescheduler(selected_list):
    rescheduled_list = []

    for item in selected_list:
        if item == "destination":
            rescheduled_list.append(list_item_randomnizer(destination_list))
        elif item == "restaurant":
            rescheduled_list.append(list_item_randomnizer(restaurant_list))
        elif item == "transportation":
            rescheduled_list.append(list_item_randomnizer(transportation_list))
        elif item == "entertainment":
            rescheduled_list.append(list_item_randomnizer(entertainment_list))
        else:
            print("Error in day_trip_reschedulere")

    return rescheduled_list

#Generates a random trip list with a destination, restaurant, transportation method, and entertainment.
def day_trip_generator(destination_list, restaurant_list, transportation_list, entertainment_list):
    trip_list = []

    trip_list.append(list_item_randomnizer(destination_list))
    trip_list.append(list_item_randomnizer(restaurant_list))
    trip_list.append(list_item_randomnizer(transportation_list))
    trip_list.append(list_item_randomnizer(entertainment_list))

    return trip_list

#Prints the instructions
def print_instructions():
    instructions =  """\n\nHello this program will generate a random list and give you the option to re-randomnize
                        parts of the list that you don't like."""
    print(instructions)

#Prints goodbye
def print_goodbye():
    goodbye = """\n\nGoodbye I hope you have a wonderful day and sorry if it was an expensive trip..."""
    print(goodbye)
