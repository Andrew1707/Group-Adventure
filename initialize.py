from room import room

#Baement Stuff
laundry = room("Laundry Room")
cellar = room("Wine Cellar")
butchers = room("Butcher's Quarters")
furnace = room("Furnace Room")
stairs1 = room("Stairs from basement and first floor")

#First Floor
gallery = room("Art Gallery")
dining = room("Dining Room")
kitchen = room("Kitchen")
sunroom = room("Sunroom")
pantry = room("Pantry")
bath1 = room("Bathroom")
stairs2 = room("Stairs between first and second floor")

#Second Floor
bed1 = room("Bedroom")
master = room("Master Bedroom")
guest = room("Guest Bedroom")
library = room("Library")
bath2 = room("Master Bathroom")
bath3 = room("Bathroom")

#Outside
maze = room("The Maze")
garden = room("The Garden")
shed = room("Shed")
graveyard = room("Graveyard")

kitchen.nearby([dining, gallery, pantry])
gallery.nearby([bath1, kitchen, dining])