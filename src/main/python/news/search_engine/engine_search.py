import requests
from bs4 import BeautifulSoup

STR_TO_REPLACE = "{{REPLACE}}"

google_search_tplte = f"https://google.com/search?q={STR_TO_REPLACE}"
duck_search_tplte = f"http://duckduckgo.com/?q={STR_TO_REPLACE}&t=h_&iar=news&ia=news"

keywords = ['leicester', 'champion']
keywords = ['el', 'capitan']

mysearch = duck_search_tplte.replace(STR_TO_REPLACE, '+'.join(keywords))

print(mysearch)
resp = requests.get(mysearch)

soup = BeautifulSoup(resp.text, "html5lib")
print(soup.prettify())
print('done')