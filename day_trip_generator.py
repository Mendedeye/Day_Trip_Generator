import random

destination_list = ["New York City", "Toranto", "Miami", "London", "Paris", "Moscow", "Death Valley", "Detroit", "Las Vagas", "Mexico City"]
restaurant_list = ["McDonalds", "Ramsy's Steakhouse", "Crumble Cookies", "Wendies", "Chick-Fil-A", "Sonic", "Cracker Barrel", "Outback"]
transportation_list = ["Semi-truck", "SUV", "Sports Car", "Boat", "Plane", "Scooter", "Bike", "Train", "Helecopter"]
entertainment_list = ["Rave", "Classical Ball", "Magician", "Inspirational Speaker Convention", "Football Game", "MMA Fight", "Music Concert"]

#main()
def main(destination_list, restaurant_list, transportation_list, entertainment_list):
    trip_list = []
    user_input = ""
    user_choice_change = []
    
    print_instructions
    trip_list = day_trip_generator(destination_list, restaurant_list, transportation_list, entertainment_list)
    print_trip_list(trip_list)
    user_input = get_user_choice_input

    while user_input.lower == "n":
        user_choice_change = trip_choice_changer
        trip_list = day_trip_rescheduler
        user_input = get_user_choice_input
    
    print_final_list
    print_goodbye

#Prints the instructions
def print_instructions():
    instructions =  """\n
        Hello this program will generate a random list of a destination, 
        restaurant, method of transportation and entertainment
        Then it will give you the option to re-randomnize
        parts of the list that you would like to change."""
    print(instructions)

#Generates a random trip list with a destination, restaurant, transportation method, and entertainment.
def day_trip_generator(destination_list, restaurant_list, transportation_list, entertainment_list):
    trip_list = []

    trip_list.append(list_item_randomnizer(destination_list))
    trip_list.append(list_item_randomnizer(restaurant_list))
    trip_list.append(list_item_randomnizer(transportation_list))
    trip_list.append(list_item_randomnizer(entertainment_list))

    return trip_list

#Takes in a list finds what needs re-randomnized and returns the re-randomnizes list.
def day_trip_rescheduler(selected_list):
    rescheduled_list = []

    for item in selected_list:
        if item.lower == "destination":
            rescheduled_list.append(list_item_randomnizer(destination_list))
        elif item.lower == "restaurant":
            rescheduled_list.append(list_item_randomnizer(restaurant_list))
        elif item.lower == "transportation":
            rescheduled_list.append(list_item_randomnizer(transportation_list))
        elif item.lower == "entertainment":
            rescheduled_list.append(list_item_randomnizer(entertainment_list))

    return rescheduled_list

#Selects and returns a random item from a list
def list_item_randomnizer(selected_list):
    selected_item = random.choice(selected_list)
    return selected_item
    
#Takes in a one string input from user
def get_user_choice_input():
    return input("Are you satisfied with your choices (y/n): ")

#get_user_choice_input
def trip_choice_changer():
    user_decisions = []
    user_choice = ""

    print("Which options would you like to change?")
    print("Destination, Restaurant, Entertainment, Transportation ")
    print("(please press enter after every item and done if that's all you want changed):")

    user_choice = input()

    while user_choice != "done":
        user_decisions.append(user_choice)
        user_choice = input
    
    return user_decisions

#Prints the trip list
def print_trip_list(selected_list):
    print(selected_list)

#Prints the final trip list 
def print_final_list(selected_list):
    print(f"You will be going to {selected_list[0]}, eating at {selected_list[1]}, taking a {selected_list[2]}, and attending a {selected_list[3]}!!!")

#Prints goodbye
def print_goodbye():
    goodbye = """\n\nGoodbye I hope you have a wonderful day and sorry if it was an expensive trip..."""
    print(goodbye)