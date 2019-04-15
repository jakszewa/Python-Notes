# Checking while,if & for loops knowledge
# New is FUNCTION

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                print(int(attempt))
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
            print(int(attempt))
    
    if attempt == 3:
        print('The correct answer is '+answer)

score = 0

print('Guess the Animal!')

guess1 = input('Which bear lives at the North Pole?')
check_guess(guess1, 'Polar Bear')

guess2 = input('Which is the fastest land animal?')
check_guess(guess2, 'Cheetah')

guess3 = input('Which is the largest animal?')
check_guess(guess3, 'blue whale')

print('Your score is '+ str(score))

'''
...
while still_guessing and attempt < 3:
if guess.lower() == answer.lower():
print('Correct Answer')
score = score + 3 – attempt
still_guessing = False
else:
if attempt < 2:
...

Better score for fewer attempts
Reward the player for getting the answer right with
fewer guesses. Give 3 points if they get it in one try,
2 points for needing two attempts, and 1 point for
using all three chances. Make this change to the line
that updates the score. Now it will give 3 points minus
the number of unsuccessful attempts. If the player
gets the answer right first time, 3 – 0 = 3 points are
added to their score; on the second guess, it’s 3 – 1 = 2
points; and on the third guess, it’s 3 – 2 = 1 point.

'''