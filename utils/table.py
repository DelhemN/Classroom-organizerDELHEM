from typing import List

class Seat():
    def __init__(self) -> None:
        self.free: bool = self.free
        self.occupant: str = ""
    
    def set_occupant(self, name: str):
        if self.free == True:
            self.occupant == name
    
    def remove_occupant(self) -> str:
        if self.free == False:
            name = self.occupant
            self.occupant = ""
        return name

class Table():
    def __init__(self) -> None:
        self.capacity: int = self.capacity
        self.seats: List[Seat] = self.seats

    def has_free_spot(self) -> bool:
        for seat in self.seats:
            if seat.free == True:
                return True
        return False

    def assign_seat(self, name: str):
        for seat in self.seats:
            if seat.free == True:
                seat.occupant == name
                break
    
    def left_capacity(self) -> int:
        free_seats: int = 0
        for seat in self.seats:
            if seat.free == True:
                free_seats += 1
        return free_seats