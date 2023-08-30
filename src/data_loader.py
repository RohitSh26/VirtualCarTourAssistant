import pandas as pd
from typing import Any


class DataLoader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def load_data(self) -> Any:
        """Load and preprocess data"""
        column_names = [
            "buying",
            "maint",
            "doors",
            "persons",
            "lug_boot",
            "safety",
            "class",
        ]

        df = pd.read_csv(self.file_path, header=None, names=column_names)

        # TODO: preprocessing

        return df


if __name__ == "__main__":
    loader = DataLoader("data/car.data")
    data = loader.load_data()
    print(data.head())
