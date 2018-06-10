from player import player
from room import room
from initialize import *

tandrew = player("Tandrew", "Noob")
caleb = player("Caleeb", "boss")

kitchen.enter(caleb)

def run():
    resp = input("Where do you want to go? ")
    for room in caleb.location.adjacent:
        if resp == room.name:
            room.enter(caleb)
    run()

run()
