class room:
    def __init__(self, name):
        self.name = name
        self.occupants = []
    
    def enter(self, player):
        self.occupants.append(player)
    
    def leave(self, player):
        self.occupants.remove(player)

    def print(self):
        print(self.name)
        for i in self.occupants:
            print(i.name)