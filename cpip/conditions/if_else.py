#Branching
'''
Computers often need to make decisions about
which parts of a program to run. This is because
most programs are designed to do different
things in different situations. The route through
the program splits like a path branching off into
side paths, each leading to a different place.
'''
'''
One branch
The simplest branching command is an if
statement. It only has one branch, which
the computer takes if the condition is True.
This program asks the user to say if it’s
dark outside. If it is, the program pretends
that the computer is going to sleep! If it’s
not dark, is_dark == 'y' is False, so the
“Goodnight!” message isn’t displayed.
'''

is_dark = input('Is it dark outside? (y/n) ')
if is_dark == 'y':
    print('GoodNight!')

'''
Two branches
Do you want a program to do one thing if
a condition’s True and another thing if it’s
False? If so, you need a command with two
branches, called an if-else statement.
This program asks if the user has tentacles.
If they answer “Yes”, it decides they must
be an octopus! If they answer “No”, it
decides they’re human. Each decision
prints a different message.
'''

tentacles = input('Do you have Tentacles? (y/n) ')
if tentacles == 'y':
    print('I never knew octopuses could type')
else:
    print('Greetings, human!')

'''
Multiple branches
When there are more than
two possible paths, the
statement elif (short for
“else-if”) comes in handy. This
program asks the user to type
in the weather forecast: either
“rain”, “snow”, or “sun”. It then
chooses one of three branches
and weather conditions.
'''

weather = input('What is the forecast for today? (rain/snow/sun)')

if weather == 'rain':
    print('Remember your umbrella!')
elif weather == 'snow':
    print('Remember your wooly gloves!')
else:
    print('Remember your sunglasses')

'''
An elif statement must always come after if and
before else. In this code, elif checks for snow only
when the condition set by the if statement is False.
You could insert additional elif statements to check
for more types of weather.
'''