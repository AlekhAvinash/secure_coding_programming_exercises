#Open the csv_practice_users.csv doc
#Retrieve all names that start with an S
#Add the ages of all the users print the total
#Retrieve the phone number of the user Jay 

import csv

lst = []
ctr = 0
phn = ""

with open("csv_practice_users.csv", "r") as f:
    out = csv.DictReader(f)
    for i in out:
        if i["Name"][0] == "S":
            lst += [i["Name"]]

        ctr += int(i["Age"])

        if i["Name"] == "Jay":
            phn = i["Phone_Number"]

print(f"Names starting with S: {lst}")
print(f"Total age: {ctr}")
print(f"Jay's Phn: {phn}")