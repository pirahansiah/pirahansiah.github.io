import json
import os
from openaimini import lambda_handler  # Import your Lambda function
import os
from dotenv import load_dotenv


# Set environment variables
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
os.environ['TELEGRAM_BOT_TOKEN'] = 'your_telegram_bot_token'

# Simulate an event from API Gateway
def create_test_event(message_text):
    return {
        'body': json.dumps({
            'update_id': 123456789,
            'message': {
                'message_id': 1,
                'from': {
                    'id': 123456789,
                    'first_name': 'Test',
                    'last_name': 'User',
                    'username': 'testuser'
                },
                'chat': {
                    'id': 123456789,
                    'type': 'private'
                },
                'date': 1623456789,
                'text': message_text
            }
        })
    }

# Test the Lambda function
def test_lambda():
    test_message = "Hello, ChatGPT!"
    event = create_test_event(test_message)
    context = {}  # You can create a mock context object if needed

    response = lambda_handler(event, context)
    print(f"Lambda function response: {response}")

if __name__ == "__main__":
    test_lambda()
