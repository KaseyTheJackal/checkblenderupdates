import requests
import os
from bs4 import BeautifulSoup

page = requests.get("https://builder.blender.org/download/daily")
soup = BeautifulSoup(page.content, 'html.parser')

last = soup.find_all('a', title="Download darwin 64bit dmg file", href=True)[-1]

download =  str(last['href'])

fileSave = download.split('/', 5)[5]

os.system("osascript -e 'display notification \"Downloading...\" with title \"New Blender version available\"'")
os.system("cd ~/Downloads && curl -o  " + fileSave + " " + download)
os.system("osascript -e 'display notification \"Download completed.\" with title \"New Blender version available\"'")
os.system("cd ~/Downloads && hdiutil attach " + fileSave)
os.system("cd /Volumes/Blender && cp -r Blender.app /Applications")
