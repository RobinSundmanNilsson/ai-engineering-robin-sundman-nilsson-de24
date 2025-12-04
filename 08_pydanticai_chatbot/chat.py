from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

class JokeChatBot:
    def __init__(self):
        self.agent = Agent(
            "google-gla:gemini-2.5-flash",
            system_prompt="You're a programming nerd, always answer with a programming joke. Also add a few emojis to your answers to keep it lighthearted!",
        )

        self.result = None

    def chat(self, prompt: str) -> dict:
        message_history = self.result.all_messages() if self.result else None

        self.result = self.agent.run_sync(prompt, message_history=message_history)

        return {"user": prompt, "bot": self.result.output}
    
if __name__ == "__main__":
    chatbot = JokeChatBot()
    result = chatbot.chat("Hello, how are you?")
    print(result)

    result = chatbot.chat("What did I ask first?")
    print(result)