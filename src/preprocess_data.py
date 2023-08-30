from sklearn.model_selection import train_test_split


def preprocess_data(input_txt, train_txt, val_txt):
    # Read the conversational data from the text file
    with open(input_txt, "r") as f:
        data = f.read()

    # Split the data into separate conversations based on the '---' separator
    conversations = data.strip().split("---\n")

    # Split the data into training and validation sets (80% training, 20% validation)
    train_conversations, val_conversations = train_test_split(
        conversations, test_size=0.2, random_state=42
    )

    # Convert the list of conversations back into string format
    train_data = "---\n".join(train_conversations)
    val_data = "---\n".join(val_conversations)

    # Save the training and validation data to separate text files
    with open(train_txt, "w") as f:
        f.write(train_data)

    with open(val_txt, "w") as f:
        f.write(val_data)

    print(f"Training data has been saved to '{train_txt}'")
    print(f"Validation data has been saved to '{val_txt}'")


if __name__ == "__main__":
    input_txt = "data/conversational_data.txt"  # Input text file name
    train_txt = "data/train_data.txt"  # Output text file for training data
    val_txt = "data/val_data.txt"  # Output text file for validation data
    preprocess_data(input_txt, train_txt, val_txt)
