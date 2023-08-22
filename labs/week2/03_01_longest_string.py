#!/usr/bin/python3
# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)




longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"


# Now that you know what the longest word is, print it out in an f-string below

# adding variables to a list
lst = [	longest_finnish_word,
		longest_german_word,
		longest_hungarian_word,
		strong_password
	]

# marking their corresponding lengths
lst = [(len(i), i) for i in lst]

# finding the string with largest length
out = sorted(lst, key = lambda a: a[0], reverse = True)[0][1]

print(f"The largest variable is: \t{out}")