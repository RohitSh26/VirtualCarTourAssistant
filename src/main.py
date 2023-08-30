from data_loader import DataLoader
from car import Car
from virtual_tour import VirtualTour
from chat_bot import ChatBot


def main():
    # Initialize DataLoader and load data
    data_loader = DataLoader("data/car.data")
    data = data_loader.load_data()
    print(f"Data loaded:\n{data.head()}")

    # Initialize other components (for demonstration)
    car1 = Car("Toyota", "Camry", 2022, {"Engine": "V6", "Color": "Red"})
    car2 = Car("Honda", "Civic", 2021, {"Engine": "I4", "Color": "Blue"})
    tour = VirtualTour([car1, car2])
    chat_bot = ChatBot("path/to/nanoGPT/model")

    # Start the application logic
    print("Starting the virtual tour...")
    tour.start_tour()
    user_query = "Tell me more about the engine."
    response = chat_bot.respond(user_query)
    print(f"ChatBot response: {response}")


if __name__ == "__main__":
    main()
