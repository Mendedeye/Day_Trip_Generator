import random

destination_list = ["New York City", "Toranto", "Miami", "London", "Paris", "Moscow", "Death Valley", "Detroit", "Las Vagas", "Mexico City"]
restaurant_list = ["McDonalds", "Ramsy's Steakhouse", "Crumble Cookies", "Wendies", "Chick-Fil-A", "Sonic", "Cracker Barrel", "Outback"]
transportation_list = ["Semi-truck", "SUV", "Sports Car", "Boat", "Plane", "Scooter", "Bike", "Train", "Helecopter"]
entertainment_list = ["Rave", "Classical Ball", "Magician", "Inspirational Speaker", "Football", "MMA Fight", "Music Concert"]

#Selects and returns a random item from a list
def list_item_randomnizer(selected_list):
    selected_item = random.choice(selected_list)
    return selected_item
#Takes in a one string input from user
def user_input():
    return input("Are you satisfied with your choices (yes/no): ")
