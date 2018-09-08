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
stairs2 = room("Down the stairs between first and second floor")

#Second Floor
bed1 = room("Boy Bedroom")
master = room("Master Bedroom")
bed2 = room("Girl Bedroom")
library = room("Library")
bath2 = room("Bathroom")
stairs3 = room("Up the stairs between the first and second floor")


#Outside
maze = room("The Maze")
garden = room("The Garden")
shed = room("Shed")
graveyard = room("Graveyard")

laundry.nearby([cellar,furnace,stairs2])
furnace.nearby([laundry,butchers])
butchers.nearby([cellar,furnace])
cellar.nearby([stairs1,butchers,laundry])
stairs1.nearby([cellar,dinning])

kitchen.nearby([dining, gallery, pantry])
gallery.nearby([kitchen, stairs2])
pantry.nearby([kitchen])
dinning.nearby([sunroom,bath1,stairs1])
bath1.nearby([dinning])
sunroom.nearby([stairs2,dinning])
stairs2.nearby([stairs3,sunroom,gallery,laundry])

stairs3.nearby([bed1,bed2,master,bath2,stairs2,library])
master.nearby([stairs3])
bed1.nearby([stairs3,])
bed2.nearby([stairs3])
library.nearby([stairs3])
bath2.nearby([stairs3])


   
