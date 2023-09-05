# write rock-paper-scissors game in python

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random, time

def get_user_choice(rpt):
    while True:
        try:
            chs = int(input(f"\n{'Keep going!' if rpt else 'Welcome!'}\nEnter your choice\n[1] rock\n[2] paper\n[3] scissors\n[4] Quit\n> ")) - 1
        except:
            chs = -1
        if chs in range(4):
            return chs
        else:
            print("Invalid input. Please enter an integer between 1 and 4.")

def determine_winner(usr, cmp):
    if usr == cmp:
        return "It's a tie!"
    elif usr == (cmp-1)%3:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    win = 0
    dir = {0: "Rock", 1: "Paper", 2: "Scissor"}
    rpt = 0
    while True:
        usr = get_user_choice(rpt)
        if usr == 3: break
        cmp = random.randint(0, 2)

        print(f"You chose: {dir[usr]}\nCmp chose: {dir[cmp]}")
        time.sleep(1)

        result = determine_winner(usr, cmp)
        win += int(result == "You win!")
        rpt += 1
        input(f"{result} You won {win} times in {rpt} games.")
    print("Quiting..")

if __name__ == "__main__":
    main()

# you can map each of rock / paper / scissors to an integer from 1 - 3
