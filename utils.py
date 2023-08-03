from bs4 import BeautifulSoup
import requests
import markdown
from datetime import datetime
import os

from config import start_url, target_url
crawled = set() 
def crawl(url):
    headers = {"User-Agent": "Mozilla/5.0"} 
    response = requests.get(url, headers=headers)
    return response.text

def parse(html):
    soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
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
            
        if href.startswith(target_url) and href not in crawled:
            links.append(href)
            crawled.add(href)
            
    return links

def save_file(content):
    outputs_dir = 'outputs'
    if not os.path.exists(outputs_dir):
        os.makedirs(outputs_dir)

    filename = f"contents_{datetime.now().strftime('%Y%m%d%H%M')}.md"
    with open(os.path.join("outputs", filename), "w", encoding='utf-8') as f:
        f.write(content)