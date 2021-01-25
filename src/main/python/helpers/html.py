from typing import Dict, List


def make_simple_html(titles_and_links: Dict):
    htmltext = '''
    <html>
        <head><title>Simple News Link Scrapper</title></head>
        <body>
            {NEWS_LINKS}
        </body>
    </html>
    '''

    news_links = '<ol>'
    for link, title in titles_and_links.items():
        news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n\n\n".format(link, title) + "<br>"

    news_links += '</ol>'

    htmltext = htmltext.format(NEWS_LINKS=news_links)
    return htmltext


if __name__ == "__main__":
    dummy_data = {'This is Article 1': 'www.google.com', 'This is Article 2': 'www.wikipedia.com'}
    simple_html = make_simple_html(dummy_data)
    print(simple_html)
