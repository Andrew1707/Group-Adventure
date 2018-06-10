class player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def move(self, room):
        self.location = room
        print("Moved to "+ room.name)
        print("Nearby Rooms:")
        for room in self.location.adjacent:
            print(room.name)