# TAGS: .format() function

formatter = "{} {} {} {}"       # variable

print(formatter.format(1, 2, 3, 4))     # putting values in variable using format function
print(formatter.format("one", "two", "three", "four"))  # {} is equal to values we are putting it
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))     # if we don't put values inside {} they are printed as it is

print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))