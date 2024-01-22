
url = "https://www.tiziran.com"
file_path = "tiziran.txt"
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
def is_valid_url(url, base_url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme) and url.startswith(base_url)

def get_all_website_links(url):
    urls = set()
    base_url = "{0.scheme}://{0.netloc}".format(urlparse(url))
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        if not is_valid_url(href, base_url):
            continue
        urls.add(href)
    return urls

def crawl_and_save(url, file_path):
    all_urls = get_all_website_links(url)
    with open(file_path, 'w', encoding='utf-8') as file:
        for page_url in all_urls:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            file.write(f"\nURL: {page_url}\n\n{text}\n")
            file.write("\n" + "-"*100 + "\n")
crawl_and_save(url, file_path)
