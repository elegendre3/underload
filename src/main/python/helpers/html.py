from typing import Dict, List, Tuple


class Icons(object):
    culture = '<i class="fas fa-seedling" style="color:#C83E4D;text-shadow:0.6px 0.6px 0.6px #000000;"></i>'
    person = '<i class="fas fa-user" style="color:#C83E4D;text-shadow:0.6px 0.6px 0.6px #000000;"></i>'
    science = '<i class="fas fa-graduation-cap" style="color:#C83E4D;text-shadow:0.6px 0.6px 0.6px #000000;"></i>'
    sports = '<i class="fas fa-biking" style="color:#C83E4D;text-shadow:0.6px 0.6px 0.6px #000000;"></i>'

    brain = '<i class="fas fa-graduation-cap" style="color:#C83E4D;text-shadow:0.6px 0.6px 0.6px #000000;"></i>'
    user_border = '<i class="far fa-user" style="color:#C83E4D;text-shadow:0.6px 0.6px 0.6px #000000;"></i>'
    address_card = '<i class ="fas fa-address-card" style="font-size:20px;color:#C83E4D;"></i>'

    map = {
        'culture': culture,
        'person': person,
        'science': science,
        'sports': sports,
    }


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
    def advanced_html(articles: List[Dict], title: str = "Headlines"):
        article_template = '''
            <div>
                <h4>{ARTICLE_TITLE}</h4>
                <a href={ARTICLE_LINK} target='_blank' class="btn-primary">{ARTICLE_TEXT}</a>
            </div>
            <br>
        '''

        #                 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        advanced_html_template = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{TITLE}</title>
                <link rel="stylesheet" href="style.css">
            </head>
                <body>
                    <div class="container">
                        <h1>- {TITLE} -</h1>
                        <br>
                        <div>
                            {ARTICLES}
                        </div>
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

    @staticmethod
    def style_html(articles: List[Tuple[Dict, List[str]]], title: str = "Headlines", tags: List[str] = ()):

        article_html = '''<div class="article">
                    <div class="article-content">
                        <h2>{ARTICLE_TITLE}</h2>
                        <h3>{ARTICLE_AUTHOR}</h3>
                        <a href={ARTICLE_LINK} target='_blank' class="btn-article">See More</a>
                        {ICONS}
                    </div>
                </div>
                '''
        base_html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{TITLE}</title>
        <link rel= "stylesheet" type= "text/css" href= "{CSS_SOURCE}">
        <script src="https://kit.fontawesome.com/88a8ba13d4.js" crossorigin="anonymous"></script>
    </head>
    <body>
        <div class="container">
            <h1>- {TITLE} -</h1>
            <div class="all-articles">
                {ARTICLES}                                    
            </div>
        </div>
    </body>
</html>
'''

        articles_html = ''
        for article, tags in articles:
            articles_html += article_html.format(
                ARTICLE_TITLE=article['title'],
                ARTICLE_AUTHOR=article['author'],
                ARTICLE_LINK=article['url'],
                ICONS='\n'.join([Icons.map[tag] for tag in tags])
            )

        htmltext = base_html.format(
            TITLE=title,
            ARTICLES=articles_html,
            CSS_SOURCE=" {{url_for('static',filename='styles/style.css')}} ",
        )
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
