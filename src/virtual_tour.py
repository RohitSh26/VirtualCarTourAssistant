from typing import List
from car import Car


class VirtualTour:
    def __init__(self, cars: List[Car]) -> None:
        self.cars = cars

    def __repr__(self) -> str:
        return f"VirtualTour(cars={self.cars})"

    def start_tour(self) -> None:
        """Method to start the virtual tour."""
        for car in self.cars:
            print(car.display_features())


if __name__ == "__main__":
    toyota = Car("Toyota", "Camry", 2022, {"Engine": "V6", "Color": "Red"})
    honda = Car("Honda", "Civic", 2021, {"Engine": "I4", "Color": "Blue"})
    tour = VirtualTour([toyota, honda])
    tour.start_tour()
