# TAGS: strings, f function, .format()
# How to use f & .format() function to insert varibale inside a variable


types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}" # embeding variable inside variable, we have defined the variable

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"   # embeding variable inside variable, joke_evaluation is a variable, 
                                                    # inside it we are using {} to put one more variable, but we are not defining it

print(joke_evaluation.format(hilarious))            # we are using .format function to put variable value inside a variable

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)