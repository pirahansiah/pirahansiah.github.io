
YOUR_SITE_URL = "https://pirahansiah.com"
YOUR_APP_NAME = "Farshid Pirahansiah"
import asyncio
import aiohttp
from collections import deque

# It seems like you're trying to set the OPENROUTER_API_KEY directly via input.
# This approach is generally insecure for API keys. Consider using environment variables
# or another secure method for handling keys in production code.
# For demonstration purposes, we'll proceed as if the key is directly inputted here.
 # input('Enter your OpenRouter API Key: ')

class OpenRouterChatApp:
    def __init__(self):
        self.session = None
        self.selected_model = "openrouter/auto"  # Default model; adjust as needed
        self.conversation_history = deque(maxlen=30)
        self.semaphore = asyncio.Semaphore(10)

    async def init_session(self):
        self.session = aiohttp.ClientSession()

    async def close_session(self):
        await self.session.close()

    async def get_chat_completion(self, user_input):
        async with self.semaphore:
            self.add_to_conversation_history("user", user_input)
            api_url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Referer": YOUR_SITE_URL,  # Adjust as needed
                "X-Title": YOUR_APP_NAME,  # Adjust as needed
            }
            data = {
                "model": self.selected_model,
                "messages": list(self.conversation_history),
            }

            async with self.session.post(url=api_url, headers=headers, json=data) as response:
                response.raise_for_status()
                api_result = await response.json()
                return api_result['choices'][0]['message']  # Assuming the API response structure

    def add_to_conversation_history(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def select_model(self):
        models = [
            "openrouter/auto", "openai/gpt-3.5-turbo", "neversleep/noromaid-mixtral-8x7b-instruct",
            "mistralai/mistral-7b-instruct", "nousresearch/nous-capybara-7b", "openchat/openchat-7b",
            "gryphe/mythomist-7b", "openrouter/cinematika-7b", "rwkv/rwkv-5-world-3b", "recursal/rwkv-5-3b-ai-town"
        ]

        # print("Available Models:")
        # for idx, model in enumerate(models, start=1):
        #     model_name = model.split("/")[-1].replace("-", " ").title()
        #     print(f"{idx}. {model_name}")

        self.selected_model='nousresearch/nous-capybara-7b'
        # while True:
        #     try:
        #         choice = int(input("Select a model (enter the corresponding number): "))
        #         if 1 <= choice <= len(models):
        #             self.selected_model = models[choice - 1]
        #             print(f"Selected Model: {self.selected_model}")
        #             break
        #         else:
        #             print("Invalid choice. Please enter a valid number.")
        #     except ValueError:
        #         print("Invalid input. Please enter a number.")

    async def main(self):
        print("Welcome to the Turbo Chat!")
        await self.init_session()
        self.select_model()

        try:
            while True:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Exiting the app. Goodbye!")
                    break

                print("Processing...")
                assistant_response = await self.get_chat_completion(user_input)
                content = assistant_response.get('content', '')
                print(content.replace('\n', '\n'))
                #print(f"Assistant: {assistant_response}\n")  # Updated to correctly print the response

        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting the app. Goodbye!")
        finally:
            await self.close_session()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(OpenRouterChatApp().main())
