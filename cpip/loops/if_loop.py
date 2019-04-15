#For loops

'''
When you know how many times you want to run a
block of code, you can use a for loop.
'''

for counter in range(1, 11):
    print('Emma\'s Room - Keep Out!!!')

'''
Loop variable
The loop variable keeps track of how many times we’ve gone
around the loop so far. The first time round it’s equal to the first
number in the list specified by range(1, 11). The second time
around it’s equal to the second number in the list, and so on.
When we’ve used all the numbers in the list, we stop looping.
'''
'''
Range
In Python code, the word “range”
followed by two numbers within
brackets stands for “all the
numbers from the first number to
one less than the second number”.
So range(1, 4) means the
numbers 1, 2, and 3—but not 4.
In Emma’s “Keep Out” program,
range(1, 11) is the numbers
1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.
'''