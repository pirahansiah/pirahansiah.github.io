import json
import os
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_API_KEY']

# Set up Telegram bot token
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

def lambda_handler(event, context):
    # Parse the incoming event from API Gateway
    body = json.loads(event['body'])
    
    # Create a Telegram Update object
    update = Update.de_json(body, None)
    
    # Process the update
    response = process_update(update)
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def process_update(update):
    # Extract the message text
    message_text = update.message.text
    
    # Process the message and get a response from OpenAI
    response = get_openai_response(message_text)
    
    # Send the response back to Telegram
    send_telegram_message(update.message.chat_id, response)
    
    return {'message': 'Message processed successfully'}

def get_openai_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

def send_telegram_message(chat_id, text):
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.bot.send_message(chat_id=chat_id, text=text)

# Additional helper functions can be added here for more complex interactions