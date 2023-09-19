from typing import List


class Seat:
    def __init__(self) -> None:
        self.free: bool = True
        self.occupant: str = ""

    def __str__(self) -> str:
        return self.occupant

    def __repr__(self) -> str:
        return self.occupant

    def set_occupant(self, name: str):
        """
        Assign a person to a free seat
        """

        if self.free:
            self.occupant = name

    def remove_occupant(self) -> str:
        """
        Remove a person from a seat
        """

        if not self.free:
            name = self.occupant
            self.occupant = ""
        return name


class Table:
    def __init__(self, capacity=4) -> None:
        self.capacity: int = capacity
        self.seats: List[Seat] = [Seat() for _ in range(capacity)]

    def __str__(self) -> str:
        return f"{self.seats}"

    def __repr__(self) -> str:
        return f"{self.seats}"

    def has_free_spot(self) -> bool:
        """
        Check if at least one seat is free at the table
        """

        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name: str):
        """
        Assign someone to a seat at the table
        """

        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                break

    def left_capacity(self) -> int:
        """
        Count how many free seat are available
        """

        free_seats: int = 0
        for seat in self.seats:
            if seat.free:
                free_seats += 1
        return free_seats
