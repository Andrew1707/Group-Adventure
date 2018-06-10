class room:
    def __init__(self, name):
        self.name = name
        self.occupants = []

    def nearby(self, rooms):
        self.adjacent = rooms   #Accepts an array of rooms

    def enter(self, player):
        self.occupants.append(player)
        player.move(self)
    
    def leave(self, player):
        self.occupants.remove(player)

    def list(self):
        print(self.name+":")
        for i in self.occupants:
            print(i.name)