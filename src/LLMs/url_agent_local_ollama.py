# import asyncio
# from scrapegraphai.graphs import SmartScraperGraph
# from ollama import AsyncClient

# model_phi3 = 'phi3'
# url = "https://pirahansiah.com"

# async def scrape_and_summarize():
#     client = AsyncClient()

#     graph_config = {
#         "ollama": {
#             "model": model_phi3,
#             "api_url": "http://localhost:11434",
#         }
#     }

#     user_prompt = f"You are a helpful assistant that summarizes the content of the website {url} in a few sentences."
#     smart_scraper_graph = SmartScraperGraph(
#         prompt=user_prompt, source=url, config=graph_config
#     )

#     result = await smart_scraper_graph.run()

#     messages = [
#         {"role": "system", "content": "You are a helpful assistant that summarizes the content of a website in a few sentences."},
#         {"role": "user", "content": result}
#     ]
#     response = await client.chat(model=model_phi3, messages=messages)
#     summary = response['message']['content']

#     print(summary)

# # Function to handle existing event loop
# def run_async_main():
#     loop = asyncio.get_event_loop()
#     if loop.is_running():
#         task = loop.create_task(scrape_and_summarize())
#         try:
#             loop.run_until_complete(task)
#         except RuntimeError:
#             # The loop is already running; use a different method to run the task
#             pass
#     else:
#         loop.run_until_complete(scrape_and_summarize())

# if __name__ == "__main__":
#     run_async_main()




######## screenshot
url2 = "https://pirahansiah.com"
from playwright.sync_api import sync_playwright
import urllib.parse
safe_url = urllib.parse.quote_plus(url2)
name_screenshot = f'web_screenshot_{safe_url}.png'
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url2)
    page.screenshot(path=name_screenshot, full_page=True)   
    browser.close()
##############


from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
# ************************************************
# Define the configuration for the graph
# ************************************************

graph_config = {
    "llm": {
        "model": "ollama/phi3",
        "temperature": 1,
        "format": "json",  # Ollama needs the format to be specified explicitly
        # "model_tokens": 2000, # set context length arbitrarily,
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
        "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    }
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the pagees with 'Jetson Nano' contents.",
    # also accepts a string with the already downloaded HTML code
    source= url2, #"https://perinim.github.io/projects",
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)

# ************************************************
# Get graph execution info
# ************************************************

graph_exec_info = smart_scraper_graph.get_execution_info()
print(prettify_exec_info(graph_exec_info))