import requests
from bs4 import BeautifulSoup


news_sites_domain = ['lemonde.fr', 'bbc.com', 'formula1.com', 'lequipe.fr']
news_sites_and_heads = {
    'lemonde.fr': ['h3'],
    'bbc.com': ['h3'],
    'lequipe.fr': ['h3'],
}
news_sites = ['http://' + x for x in news_sites_domain]

site = news_sites[0]

resp = requests.get(site)

soup = BeautifulSoup(resp.text, "html5lib")
# spans = soup.find_all('span', class_='article__title-label')
# h1 = soup.find_all('h1', {'data-layout': 'article__title'})
titles = soup.find_all(['h3'], )

for title in titles:
    link = title.parent.get('href')
    if (link) and ('http' in link):
        title_text = title.contents[-1].string
        if not title_text:
            title_text = title.text
        print(f"Title: [{title_text}]")
        print(f"Link: [{link}]")
        print()

# print(soup.prettify())
# print()
# print("#############")
# print()
# text = soup.get_text()
# print(text)
