from bs4 import BeautifulSoup
import requests
import markdown
from datetime import datetime
import os

from config import start_url, target_url

def crawl(url):
    headers = {"User-Agent": "Mozilla/5.0"} 
    response = requests.get(url, headers=headers)
    return response.text

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    text = markdown.markdown(text)
    return text

def get_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('/'): 
            href = target_url + href
        if href.startswith(target_url):
            links.append(href)
    return links

def save_file(content):
    filename = f"contents_{datetime.now().strftime('%Y%m%d%H%M')}.md"
    with open(os.path.join("outputs", filename), "w") as f:
        f.write(content)