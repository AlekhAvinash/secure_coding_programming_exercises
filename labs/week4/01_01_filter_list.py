# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3
stg1 = lambda lst: len(list(filter(lambda a: len(a)>=2,lst)))
print(stg1(['aaaa', 'a', 'ab', 'abc']))

## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
stg2 = lambda lst: len(list(filter(lambda a: len(a)>=2 and a[0]==a[-1], lst)))
print(stg2(['abc', 'xyz', 'aba', '1221']))