import json


def generate_conversations(input_json, output_txt):
    # Load the structured data from the JSON file
    with open(input_json, "r") as f:
        structured_data = json.load(f)

    # Initialize an empty string to hold the conversations
    conversations = ""

    # Generate conversations based on the structured data
    for car_info in structured_data:
        conversations += "Customer: Tell me about this car.\n"
        conversations += (
            f"Salesperson: This car is classified as '{car_info['class']}'. "
        )
        conversations += f"It has a '{car_info['features']['buying']}' buying price, "
        conversations += f"'{car_info['features']['maint']}' maintenance cost, "
        conversations += f"'{car_info['features']['doors']}' doors, "
        conversations += f"can carry '{car_info['features']['persons']}' persons, "
        conversations += f"has a '{car_info['features']['lug_boot']}' luggage boot, "
        conversations += f"and '{car_info['features']['safety']}' safety features.\n"
        conversations += "Customer: What are the safety features?\n"
        conversations += f"Salesperson: The safety features are rated as '{car_info['features']['safety']}'.\n"
        conversations += "---\n"

    # Save the conversations to a text file
    with open(output_txt, "w") as f:
        f.write(conversations)

    print(f"Conversational data has been saved to '{output_txt}'")


if __name__ == "__main__":
    input_json = "data/structured_car_data.json"  # Input JSON file name
    output_txt = "data/conversational_data.txt"  # Output text file name
    generate_conversations(input_json, output_txt)
