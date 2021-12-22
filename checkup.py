import requests
from bs4 import BeautifulSoup

page = requests.get("https://builder.blender.org/download/daily")
soup = BeautifulSoup(page.content, 'html.parser')

last = soup.find_all('li', class_="os macos")[-2]

print(last)
