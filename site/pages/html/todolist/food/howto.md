Building and Deploying a Fine-Tuned ChatGPT Model for Telegram Integration Using AWS Lambda

Steps:
Created a custom dataset for fine-tuning the ChatGPT model based on the OpenAI chat completions guide.
Uploaded the dataset to OpenAI's storage for model fine-tuning.
Fine-tuned the model using the "gpt-4o-mini-2024-07-18" as the base.
3.5. Used an AWS Lambda layer to manage dependencies due to the large size of the Lambda function. I created a folder, zipped it, and used the following command to install the required packages into the python/ directory:
bash
Copy code


pip install --platform=manylinux2014_aarch64 --implementation=cp --abi=cp39 --only-binary=:all: --target=python/ requests python-telegram-bot pyTelegramBotAPI exceptiongroup openai boto3 pydantic pydantic_core



Then, I created a custom layer with a new version and applied it across other Lambda functions to manage shared dependencies.
Developed an AWS Lambda function to facilitate communication between a Telegram bot and the fine-tuned ChatGPT model.
Set up an API Gateway to enable communication between AWS Lambda, the Telegram bot, and ChatGPT.
Created and activated a Telegram bot, using the setWebhook API to connect it with the AWS Lambda function.
Hashtags:
#AI #ChatGPT #TelegramBot #AWSLambda #LambdaLayers #FineTuning #APIGateway #MachineLearning #CloudComputing #Automation #OpenAI
