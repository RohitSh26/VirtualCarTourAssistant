class ChatBot:
    def __init__(self, model_path: str) -> None:
        self.model_path = model_path  # we will use a custom nanoGPT trained model

    def __repr__(self) -> str:
        return f"ChatBot(model_path={self.model_path})"

    def respond(self, query: str) -> str:
        """Generate a response to a user query."""

        # TODO: implementation to be added

        return f"Received your query: {query}"


if __name__ == "__main__":
    chat_bot = ChatBot("path/to/model")
    print(chat_bot.respond("Tell me more about the engine."))
