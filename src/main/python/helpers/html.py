from typing import Dict, List


class Styler(object):

    @staticmethod
    def simple_html(articles: List[Dict]):
        simple_html_template = '''
        <html>
            <head><title>Simple News Link Scrapper</title></head>
            <body>
                {NEWS_LINKS}
            </body>
        </html>
        '''

        news_links = '<ol>'
        for article in articles:
            agg_text = f"[{article['author']}] | {article['title']} | {article['description']}"
            news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n\n\n".format(article['url'], agg_text) + "<br>"
        news_links += '</ol>'

        htmltext = simple_html_template.format(NEWS_LINKS=news_links)
        return htmltext

    @staticmethod
    def advanced_html(articles: List[Dict], title: str = 'Headlines'):
        article_template = '''
            <div>
                <h4>{ARTICLE_TITLE}</h4>
                <a href={ARTICLE_LINK} target='_blank'>{ARTICLE_TEXT}</a>
            </div>
            <br>
        '''

        advanced_html_template = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{TITLE}</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
            </head>
                <body>
                    <h1>- {TITLE} -</h1>
                    <br>
                    <div>
                        {ARTICLES}
                    </div>
                </body>
            </html>
        '''

        articles_html = ''
        for article in articles:
            agg_title = f"[{article['author']}] | {article['title']}"
            articles_html += article_template.format(ARTICLE_TITLE=agg_title, ARTICLE_LINK=article['url'], ARTICLE_TEXT=article['description']) + '<br>'

        htmltext = advanced_html_template.format(TITLE=title, ARTICLES=articles_html)
        return htmltext


if __name__ == "__main__":
    dummy_data = [
        {'url': 'www.google.com', 'title': 'Title 1', 'description': 'Article description', 'author': 'J.D'},
        {'url': 'www.google.com', 'title': 'Title 2', 'description': 'Article description', 'author': 'J.K.R'},
    ]
    simple_html = Styler.simple_html(dummy_data)
    print(simple_html)

    print()
    advanced_html = Styler.advanced_html(dummy_data)
    print(advanced_html)
