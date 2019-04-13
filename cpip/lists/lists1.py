#Lists

'''
When you want to store a lot of data, or
perhaps the order of the data is important,
you may need to use a list. A list can hold
many items together and keep them in order.
Python gives each item a number that shows
its position in the list. You can change the
items in the list at any time.
'''

'''
Multiple variables
Imagine you’re writing a multiplayer game
and want to store the names of the players
in each team. You could create a variable for
each player, which might look like this...
'''

rockets_player_1 = 'Rory'
rockets_player_2 = 'Rav'
rockets_player_3 = 'Rachel'
planets_player_1 = 'Peter'
planets_player_2 = 'Pablo'
planets_player_3 = 'Polly'

print( rockets_player_1,rockets_player_2,rockets_player_3,planets_player_1,planets_player_2,planets_player_3)

'''
Put a list in a variable
...but what if there were six players per team?
Managing and updating so many variables
would be difficult. It would be better to use a
list. To create a list, you surround the items you
want to store with square brackets. Try out
these lists in the shell.
'''

rockets_players = ['Rory','Rav','Rachel','Renata','Ryan','Ruby']
planets_players = ['Peter','Pablo','Polly','Penny','Paula','Patrick']

print(rockets_players)
print(planets_players)

'''
Getting items from a list
Once your data is in a list, it’s easy to work with.
To get an item out of a list, first type the name
of the list. Then add the item’s position in the
list, putting it inside square brackets. Be careful:
Python starts counting list items from 0 rather
than 1. Now try getting different players’ names
out of your team lists. The first player is at
position 0, while the last player is at position 5.
'''

print(rockets_players[0])
print(planets_players[5])