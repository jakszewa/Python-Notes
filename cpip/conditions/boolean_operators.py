#Boolean Operators

'''
Statements about variables and values that use
the logical operators always give us a Boolean
value, such as True or False. Because of this,
these statements are called Boolean expressions.
All of our statements about pineapples and
zebras are Boolean expressions.
'''

pineapples = 5
zebras = 2

print(zebras < pineapples)      #less than
print(pineapples == zebras)     #equal to
print(pineapples > zebras)      #greater than

print(pineapples != zebras)     #not equal to

'''
Multiple comparisons
You can use and and or to combine more than one
comparison. If you use and, both parts of the comparison
must be correct for the statement to be True. If you use
or, only one part needs to be correct.
'''

#Example:

age = 10
height = 18
ans = (age > 8) and (height > 53)

print(ans)