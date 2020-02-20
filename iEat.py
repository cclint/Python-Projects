# Imports
import random

food_library = {
    "Chinese": ["Mings", "China 1", "Hong Kong Restaurant"],
    "Japanese": ["Styx", "Sumos", "Sushi Village"],
    "Mexican": ["Baha Califorina", "Habeneros", "Jaliscos"],
    "Fast Food": ["Burger King", "Arbys", "Chick-Fil-A"],
}


def greeting():
    convo = input(
        "Hi! Welcome to iEat! Rate your budget from $ - $$$. $ = cheap, $$ = moderate, $$$ = high price. If don't care about the expense, say ALL:\n"
    )
    return convo


def libraryModifier(convo: str) -> dict:
    if convo == "ALL" or convo == "all" or convo == "All":
        return food_library
    elif convo == "$":
        food_library.pop("Mexican", None)
        food_library.pop("Chinese", None)
        food_library.pop("Japanese", None)
        return food_library
    elif convo == "$$":
        food_library.pop("Japanese", None)
        return food_library
    elif convo == "$$$":
        food_library.pop("Mexican", None)
        food_library.pop("Chinese", None)
        food_library.pop("Fast Food", None)
        return food_library


def genreChooser(food_library: dict) -> str:  # randomly choose a genre
    genre = random.choice(list(food_library))
    return genre


def genreToRestaurantMatch(
    genre: str
) -> list:  # matches the randomly chosen genre to it's value
    restaurant = food_library.get(genre)
    return restaurant
 

def restaurantChooser(
    restaurant: list
) -> str:  # randomly choses an element in the restaurant list
    choice = random.choice(restaurant)
    return choice


def output(choice: str) -> str:
    dialog = "Congrats on making a choice! You have chosen {}!".format(choice)
    return dialog


def run():
    library_greeting = libraryModifier(greeting())
    genre_chooser = genreChooser(library_greeting)
    genre_to_restaurant = genreToRestaurantMatch(genre_chooser)
    restaurant_chooser = restaurantChooser(genre_to_restaurant)
    final_dialog = output(restaurant_chooser)
    return final_dialog


def main():
    print(run())


if __name__ == "__main__":
    main()

""" 

Short Term Goals:

 - TODO:

- Take in a config file instead of hard coding data
- More choices
- Add $$$$
- add number and address and hours of operation
- add some machine learning concepts, like the ability for te user to rate each random choice

Long Term Goals:

- Eventually scrape local restaurants off a search engine
- Turn into a mobile app

"""
