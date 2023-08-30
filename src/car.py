from typing import Dict


class Car:
    def __init__(
        self, make: str, model: str, year: int, features: Dict[str, str]
    ) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.features = features

    def __repr__(self) -> str:
        return f"Car(make={self.make}, model={self.model}, year={self.year}, features={self.features})"

    def display_features(self) -> str:
        """Display car features in a readable format."""
        return f"{self.year} {self.make} {self.model} has the following features: {self.features}"


if __name__ == "__main__":
    toyota_camary = Car("Toyota", "Camry", 2022, {"Engine": "V6", "Color": "Red"})
    print(toyota_camary)
    print(toyota_camary.display_features())
