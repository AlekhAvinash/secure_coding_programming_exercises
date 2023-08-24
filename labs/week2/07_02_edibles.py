# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."

# Indexing
# for c, i in enumerate(s):
#     print(c, i)

apple = s[7:12]
egg = s[26:29]
butter = s[57:63]
flour = s[68:73]
print(apple, egg, butter, flour)
print("Apple Biscuits?")
