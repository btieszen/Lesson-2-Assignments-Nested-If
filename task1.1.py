#Nested Decisions: The Adventure Game 
place = input("Choose a place: forest or cave? ")
if place == "forest":
    forest = input("climb a tree or cross a river?")
    if forest == "climb a tree":
        print("You found a bird's nest!")
    elif forest == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")