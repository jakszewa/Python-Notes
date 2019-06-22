# TAGS: \t \n """


tabby_cat = "\tI'm tabbed in."          # Adding TAB in output
persian_cat = "I'm split\non a line."   # Splitting to new line
backlash_cat = "I'm \\ a \\ cat."       # escapting sequence

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
{}
"""                                     # Using """ to split on new line
print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

print(fat_cat.format(tabby_cat))        # combining """ and .format()


testing = '''
There 
are 
single 
quoates
'''                                     # ''' can also be used instead of """

print(testing)