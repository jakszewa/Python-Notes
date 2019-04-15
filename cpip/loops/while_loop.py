#While loops
'''
What happens if you don’t know how many times
you want to repeat the code?
'''

'''
Loop condition
A while loop doesn’t have a loop variable that’s set to a
range of values. Instead it has a loop condition. This is a
Boolean expression that can be either True or False. It’s a bit
like a bouncer at a disco asking you if you’ve got a ticket. If
you have one (True), head straight for the dance floor; if you
don’t (False), the bouncer won’t let you in. In programming,
if the loop condition isn’t True, you won’t get into the loop!
'''

hippos = 0
answer = 'y'
while answer == 'y':
    hippos = hippos + 1
    print(str(hippos) + ' balancing hippos!')
    answer = input('Add another hippo? (y/n)')

    if answer == 'n':
        print(str(hippos))

'''
How it works
The loop condition in program is
answer == 'y'. This means that the user
wants to add a hippo. In the body of the
loop we add one to the number of hippos
balanced, then ask the user if they want to
add another. If they answer by typing “y”
(for yes), the loop condition is True so we
go around the loop again. If they answer “n”
(no), the loop condition is False and the
program leaves the loop.
'''

# Infinite loops

'''
Sometimes you may want a while
loop to keep going for as long as the
program is running. This kind of loop
is called an infinite loop. Lots of
video-game programs use an infinite
loop known as a main loop.
'''

'''
Into infinity
You make an infinite loop by setting the loop condition to a
constant value: True. Because this value never changes, the
loop will never exit. Try this while loop in the shell. It has no
False option, so the loop will print “This is an infinite loop!”
nonstop until you quit the program.
'''


while True:
    print('This is an Infinite loop')

#When running this comment above while loop or program will not run.
while True:
    answer = input('Are you bored yet? (y/n)')
    if answer == 'y':
        print('How rude!')
        break 

