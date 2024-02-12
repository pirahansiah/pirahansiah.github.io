
YOUR_SITE_URL = "pi"
YOUR_APP_NAME = "fp"
import requests
import json

# Ensure that the API key is correctly provided and matches the expected format for the API you're using.
# The provided "Authorization" header in the original code seems to be a placeholder or example.
# Replace it with your actual API key or token, following the service's authentication guidelines.
API_KEY = OPENROUTER_API_KEY  # Replace YOUR_API_KEY_HERE with your actual API key

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "",  # Commonly, Authorization headers are formatted as "Bearer {token}"
        # "HTTP-Referer" and "X-Title" headers are not standard for authorization and might be specific to your use case.
        # Ensure they are required by your API and correctly supported.
        "Referer": YOUR_SITE_URL,  # Typically, it's "Referer" without the "HTTP-" prefix.
        "X-Title": YOUR_APP_NAME,
    },
    json={  # Use the `json` parameter for automatic content-type handling and encoding.
        "model": "nousresearch/nous-capybara-7b:free",  # Adjust according to your needs.
        "messages": [
            {"role": "user", "content": "python code to add two numbers?"}
        ]
    }
)

# To print the response status to check if the request was successful
print(response.status_code)

# To print the response's body/content, assuming JSON format
try:
    data = response.json()  # Use `.json()` to parse the JSON response body
    print(json.dumps(data, indent=4))  # Pretty print the JSON data
except ValueError:
    print("Response content is not valid JSON")
except Exception as e:
    print(f"An error occurred: {e}")

