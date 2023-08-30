import pandas as pd
import json


def transform_data(input_csv, output_json):
    # Define attribute names and their possible values
    attribute_names = [
        "buying",
        "maint",
        "doors",
        "persons",
        "lug_boot",
        "safety",
        "class",
    ]
    attribute_values = {
        "buying": ["vhigh", "high", "med", "low"],
        "maint": ["vhigh", "high", "med", "low"],
        "doors": ["2", "3", "4", "5more"],
        "persons": ["2", "4", "more"],
        "lug_boot": ["small", "med", "big"],
        "safety": ["low", "med", "high"],
        "class": ["unacc", "acc", "good", "vgood"],
    }

    # Read the CSV file into a DataFrame
    data = pd.read_csv(input_csv, header=None, names=attribute_names)

    # Validate the data against the defined attribute values
    for attribute, values in attribute_values.items():
        if not set(data[attribute]).issubset(set(values)):
            raise ValueError(f"Invalid values found in column {attribute}")

    # Initialize an empty list to hold the structured data
    structured_data = []

    # Iterate through each row in the DataFrame to create structured data
    for index, row in data.iterrows():
        car_info = {
            "class": row["class"],
            "features": {
                "buying": row["buying"],
                "maint": row["maint"],
                "doors": row["doors"],
                "persons": row["persons"],
                "lug_boot": row["lug_boot"],
                "safety": row["safety"],
            },
        }
        structured_data.append(car_info)

    # Save the structured data to a JSON file
    with open(output_json, "w") as f:
        json.dump(structured_data, f, indent=4)


if __name__ == "__main__":
    input_csv = "data/car.data"
    output_json = "data/structured_car_data.json"
    transform_data(input_csv, output_json)
    print(f"Structured car data has been saved to '{output_json}'")
