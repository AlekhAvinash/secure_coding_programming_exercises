#Exercise

#Write a python program in which read an integer number less than 7 from user

#If the input number is greater than  or equal to 7, then print error message

#If the input is 0 print "Sunday"
#If the input is 1 print "Monday"
#If the input is 2 print "Tuesday"
#If the input is 3 print "Wednesday"
#If the input is 4 print "Thrusday"
#If the input is 5 print "Friday"
#If the input is 6 print "Saturday"

#Use if-else statements only

num = int(input("Input number: "))
if num >= 7 or num < 0:
    print("Number must be less than 7 and greater than or equal to 0!!")
else:
    if num == 0:
        print("Sunday")
    if num == 1:
        print("Monday")
    if num == 2:
        print("Tuesday")
    if num == 3:
        print("Wednesday")
    if num == 4:
        print("Thursday")
    if num == 5:
        print("Friday")
    if num == 6:
        print("Saturday")
