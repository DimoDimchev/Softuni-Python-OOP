class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):
        rooms = [room for room in self.rooms if room.number == room_number]
        if rooms:
            return rooms[0].take_room(people)

    def free_room(self, room_number):
        rooms = [room for room in self.rooms if room.number == room_number]
        if rooms:
            return rooms[0].free_room()

    def print_status(self):
        free_rooms = [free for free in self.rooms if not free.is_taken]
        hotel_guests = sum([f.guests for f in self.rooms if f.is_taken])
        print(f"Hotel {self.name} has {hotel_guests} total guests")
        print(f"Free rooms: {', '.join([str(p.number) for p in free_rooms])}")
        print(f"Taken rooms: {', '.join([str(p.number) for p in self.rooms if p not in free_rooms])}")
