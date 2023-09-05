# write a script that will "sing" a song that goes like this
#  "there are 100 jars of payasam on the counter ...... now i ate one!"
# "there are 99 jars of payasam on the counter ... now I ate one!"
#
#
# "there are 0 jars of payasam on the counter - none left to eat!"
# "now I will go vomit...."

# you must use a while loop to do it

ctr = 100
while ctr:
    ctr -= 1
    print(f"there are {ctr} jars of payasam on the counter ...... now i ate one!")
print("now I will go vomit....")