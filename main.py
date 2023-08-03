from utils import crawl, parse, get_links, save_file

from config import start_url, target_url

content = "" 
page_urls = [start_url]

while page_urls:
   # 爬取和解析 
   url = page_urls.pop(0)
   html = crawl(url)
   text = parse(html)

   # 存储
   content += "\n# " + url + "\n\n" + text
   if len(content) >= 10 * 1024 * 1024:
       save_file(content)
       content = ""

   # 下一页
   links = get_links(html)
   page_urls.extend(links)

print("Extraction finished.")