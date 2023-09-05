# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.

# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

import time

def menu(title: str, opt: list) -> int:
    try:
        chs = "\n".join(f"[{c+1}] {i}" for c, i in enumerate(opt + ["quit"]))
        time.sleep(0.7)
        return int(input(f"{title}\n{chs}\n> "))
    except:
        print(f"Only integer inputs are allowed!")
    return -1

def main():
    nme = input("Hello, Adventurer!!\nEnter name: ")
    print(f"Welcome to CLI DnD!, {nme}")

    act = 0
    swd = False
    rte = ""
    while True:
        if act not in [1, 2, 3]:
            act = menu(f"{rte}You find yourself standing in front of two doors.", ["left door", "right door"])
        

        if act == 1:
            act = menu("You enter the left door and find an empty room.", ["look around", "go back"])
            if act == 1:
                if swd:
                    print("Nothing else here..")
                    continue
                act = menu("You find a sword in the corner of the room!", ["take it!", "leave it.."])
                if act == 1:
                    swd = True
            elif act == 2:
                rte = "Returned! "
                act = 0
            else:
                continue
        
        
        elif act == 2:
            act = menu("You enter the right door and encounter a fierce dragon!", ['fight the dragon', 'go back'])                
            if act == 1:
                if swd:
                    print(f"With your sword in hand, you bravely defeat the dragon and win the game, {nme}!")
                else:
                    print(f"You don't have a sword to fight the dragon. You have been eaten. Game Over! Sry, {nme}..")
                break
            elif act == 2:
                rte = "Returned! "
                act = 0
            else:
                continue
        
        elif act == 3:
            print("Quiting..")
            break


        else:
            print("Invalid choice. Try again...")

if __name__ == "__main__":
    main()
