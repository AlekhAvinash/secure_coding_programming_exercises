# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option

while True:
    inp = int(input())
    if inp == 1:
        print("here is your first step")
    elif inp == 2:
        print("you have some steps to go")
    elif inp == 3:
        print("you are almost done")
    elif inp == 4:
        print("done")
        break
    else:
        print("it is an  invalid option")