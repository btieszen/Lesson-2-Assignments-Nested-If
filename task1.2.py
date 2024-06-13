#Nested Decisions: The Adventure Game added cave
place = input("Choose a place: forest or cave? ")
if place == "forest":
    forest = input("climb a tree or cross a river?")
    if forest == "climb a tree":
        print("You found a bird's nest!")
    elif forest == "cross a river":
        print("You found a boat!")
elif place == "cave":       
    cave = input("Do you want to light a torch or proceed in the dark ")
    if cave == "light a torch":
        print ("You found the treaure")
    elif cave== "proceed in the dark":
        print ("OUCH!!! you hit your head")
        
    