# Working with strings

'''
Coders use the word “string” for any data
made up of a sequence of letters or other
characters. Words and sentences are
stored as strings. Almost all programs use
strings at some point. Every character that
you can type on your keyboard, and even
those you can’t, can be stored in a string.
'''

name = 'Ally Alien'

print(name)

# Add two strings

greeting = 'Welcome to Earth, '

message = greeting + name

print(message)

# Length of a String

'''
You can use a handy trick, len(), to
count the number of characters in a string
(including the spaces). The command
len() is an example of what coders call a
function.
'''

print(len(message))             # get the length and print it
print(len(greeting+name))       # another way of doing it

