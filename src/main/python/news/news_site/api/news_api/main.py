import json
from pathlib import Path
import random
import requests
from typing import Dict, List

from news.news_site.api.news_api.key import get_key
from helpers.html import Styler
from helpers.interests import Interests

DEV = True

dummy_data = {'status': 'ok', 'totalResults': 38, 'articles': [
            {'source': {'id': None, 'name': 'WSB Atlanta'}, 'author': 'WSBTV.com News Staff',
             'title': 'Braves legend Hank Aaron dies at age 86, daughter says - WSB Atlanta',
             'description': 'Legendary Atlanta Brave and Major League Baseball record holder Hank Aaron died Friday at the age of 86.',
             'url': 'https://www.wsbtv.com/news/local/braves-legend-hank-aaron-dies-age-86-according-former-city-official/JXDCLYDFFVHNPC2KRNX2KBKIEM/',
             'urlToImage': 'https://www.wsbtv.com/resizer/LBlOrQAN0mQrKUzUcnC9TtYJ6Nc=/1200x628/d1hfln2sfez66z.cloudfront.net/01-22-2021/t_05decf5f564c400fa47ac027b45d612b_name_Baseball_legend_Hank_Aaron_dead_at_86_600af006fb74df5fefe89d0d_1_Jan_22_2021_15_53_58_poster.jpg',
             'publishedAt': '2021-01-22T16:06:58Z',
             'content': 'ATLANTA — He is the one man that Muhammad Ali said he idolized more than myself. He became known to the world as Hammerin Hank.\r\nLegendary Atlanta Brave and Major League Baseball record holder Hank A… [+8166 chars]'},
            {'source': {'id': None, 'name': 'NPR'}, 'author': '',
             'title': 'Lloyd Austin Confirmed As Secretary of Defense, Becomes First Black Pentagon Chief - NPR',
             'description': "Austin's near-unanimous confirmation came despite concerns raised on both sides of the aisle that he hadn't been out of uniform for the legally-mandated minimum seven-year period.",
             'url': 'https://www.npr.org/sections/president-biden-takes-office/2021/01/22/959581977/lloyd-austin-confirmed-as-secretary-of-defense-becomes-first-black-pentagon-chie',
             'urlToImage': 'https://media.npr.org/assets/img/2021/01/22/gettyimages-1290334708_wide-787df8a310af9a103e1ec3661bd09f3fa8bdef30.jpg?s=1400',
             'publishedAt': '2021-01-22T16:05:00Z',
             'content': 'Retired U.S. Army Gen. Lloyd Austin was confirmed as the next secretary of defense. He is seen above speaking after being nominated by then-President-elect Joe Biden last month.\r\nChip Somodevilla/Get… [+3284 chars]'},
            {'source': {'id': 'fox-news', 'name': 'Fox News'}, 'author': 'Jessica Napoli',
             'title': 'Gigi Hadid reveals name of baby daughter - Fox News',
             'description': 'She shares the baby with her boyfriend Zayn Malik.',
             'url': 'https://www.foxnews.com/entertainment/gigi-hadid-reveals-name-daughter',
             'urlToImage': 'https://static.foxnews.com/foxnews.com/content/uploads/2020/10/Gigi-Hadid-e1603652481325.jpg',
             'publishedAt': '2021-01-22T15:48:01Z',
             'content': 'Gigi Hadid finally revealed the name of her baby daughter whom she shares with boyfriend Zayn Malik.\r\nThe 25-year-old supermodel subtly changed her Instagram profile to read "Khai\'s mom."\r\nThe couple… [+1031 chars]'},
            {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': "Kate Sullivan, Christopher Hickey and Sean O'Key, CNN",
             'title': 'Here are the 30 executive orders and actions Biden will sign in his first three days - CNN',
             'description': "President Joe Biden is signing a flurry of executive orders, actions and memorandums aimed at rapidly addressing the coronavirus pandemic and dismantling many of President Donald Trump's policies.",
             'url': 'https://www.cnn.com/2021/01/22/politics/joe-biden-executive-orders-first-week/index.html',
             'urlToImage': 'https://cdn.cnn.com/cnnnext/dam/assets/210121094514-05-biden-executive-orders-0120-super-tease.jpg',
             'publishedAt': '2021-01-22T15:39:00Z', 'content': None},
            {'source': {'id': 'usa-today', 'name': 'USA Today'},
             'author': 'Savannah Behrmann, Bart Jansen, Christal Hayes, Nicholas Wu',
             'title': 'Politics live updates: Schumer says Trump impeachment article will go to Senate on Monday - USA TODAY',
             'description': 'Senate Majority Leader Chuck Schumer said the House will send the Senate the Trump impeachment article on Monday to start a trial',
             'url': 'https://www.usatoday.com/story/news/politics/2021/01/22/politics-live-updates-senate-wrestles-trump-impeachment-trial/6666302002/',
             'urlToImage': 'https://www.gannett-cdn.com/presto/2020/12/17/USAT/1ec764c4-8b59-4a29-b63d-54da88bc3e55-GTY_1290155881.jpg?crop=7826,4403,x0,y0&width=3200&height=1680&fit=bounds',
             'publishedAt': '2021-01-22T15:11:15Z',
             'content': "President Biden is putting into play his national COVID-19 strategy to ramp up vaccinations and testing.\r\nUSA TODAY\r\nThe Senate on Friday confirmed Lloyd Austin as the nation's first Black defense se… [+5560 chars]"},
            {'source': {'id': None, 'name': 'NPR'}, 'author': '',
             'title': 'Super Bowl LV: NFL Invites 7,500 Health Care Workers : Coronavirus Updates - NPR',
             'description': "Most of the invitees work in the central Florida area, though all of the NFL's 32 clubs will pick health care workers from their communities to receive free tickets to the sport's biggest game.",
             'url': 'https://www.npr.org/sections/coronavirus-live-updates/2021/01/22/959563778/nfl-invites-7-500-health-care-workers-to-the-super-bowl',
             'urlToImage': 'https://media.npr.org/assets/img/2021/01/22/ap_090128028868_wide-324688942a03ecf0bbaa25f7bcc770d2bc2641d5.jpg?s=1400',
             'publishedAt': '2021-01-22T14:59:00Z',
             'content': "The NFL is inviting about 7,500 healthcare workers to Super Bowl LV in Tampa, Fla.'s Raymond James Stadium, shown here in 2009.\r\nCharlie Riedel/Associated Press\r\nWhen Super Bowl LV kicks off next mon… [+2121 chars]"},
            {'source': {'id': 'nbc-news', 'name': 'NBC News'}, 'author': 'Wilson Wong',
             'title': 'Texas doctor accused of stealing vial of Covid-19 vaccine - NBC News',
             'description': 'Dr. Hasan Gokal charged with theft by a public servant after authorities said he stole a vial containing nine doses of the vaccine.',
             'url': 'https://www.nbcnews.com/news/us-news/texas-doctor-accused-stealing-vial-covid-19-vaccines-n1255281',
             'urlToImage': 'https://media4.s-nbcnews.com/j/newscms/2021_03/3444241/210122-covid-vaccine-al-0829_3835c6c6f148c0683a9edff457f069bc.nbcnews-fp-1200-630.jpg',
             'publishedAt': '2021-01-22T14:55:00Z',
             'content': 'A Texas doctor was charged Thursday with stealing a vial of the Covid-19 vaccine, according to prosecutors.\r\nDr. Hasan Gokal faces a charge of theft by a public servant after authorities said he stol… [+1656 chars]'},
            {'source': {'id': None, 'name': 'Kitco NEWS'}, 'author': 'http://www.facebook.com/kitconews',
             'title': 'Gold prices remain under pressure following strong rise in U.S. Flash PMI data - Kitco NEWS',
             'description': '(Kitco News)\xa0- The gold market remains under pressure but is seeing little movement heading into the weekend as positive economic data and improving sentiment weighs on the precious metal.',
             'url': 'https://www.kitco.com/news/2021-01-22/Gold-prices-remain-under-pressure-following-strong-rise-in-U-S-Flash-PMI-data.html',
             'urlToImage': 'https://www.kitco.com/news/2021-01-22/images/chartbw.jpg',
             'publishedAt': '2021-01-22T14:53:00Z',
             'content': "Editor's Note: With so much market volatility, stay on top of daily news! Get caught up in minutes with our speedy summary of today's must-read news and expert opinions. Sign up here! \r\n(Kitco News)\xa0… [+2072 chars]"},
            {'source': {'id': 'cnn', 'name': 'CNN'}, 'author': 'Madeline Holcombe and Jason Hanna, CNN',
             'title': 'The US can vaccinate up to 85% of adults and begin a return to normal by fall, Fauci says - CNN',
             'description': 'Despite challenges with distributing and administering Covid-19 vaccines, the US "can and should" vaccinate 70-85% of adults by the end of summer, infectious disease expert Dr. Anthony Fauci says.',
             'url': 'https://www.cnn.com/2021/01/22/health/us-coronavirus-friday/index.html',
             'urlToImage': 'https://cdn.cnn.com/cnnnext/dam/assets/210122025048-us-coronavirus-0107-super-tease.jpg',
             'publishedAt': '2021-01-22T14:49:00Z',
             'content': '(CNN)Despite challenges with distributing and administering Covid-19 vaccines, the US "can and should" vaccinate 70-85% of adults by the end of summer, infectious disease expert Dr. Anthony Fauci say… [+6010 chars]'},
            {'source': {'id': None, 'name': 'Page Six'}, 'author': 'Francesca Bacardi',
             'title': "Casey Affleck confirms he didn't throw out the Ana de Armas cutouts - Page Six",
             'description': 'He wasn’t the mystery man.',
             'url': 'https://pagesix.com/2021/01/22/casey-affleck-addresses-ben-affleck-and-ana-de-armas-breakup/',
             'urlToImage': 'https://pagesix.com/wp-content/uploads/sites/3/2021/01/casey-affleck-armas.jpg?quality=90&strip=all&w=1200',
             'publishedAt': '2021-01-22T14:49:00Z',
             'content': 'Casey Affleck has spoken out on his brother Ben Affleck’s breakup with Ana de Armas and confirmed he wasn’t the mystery man who was spotted throwing away the cardboard cutouts of the actress.\r\n“No, t… [+1494 chars]'},
            {'source': {'id': 'bleacher-report', 'name': 'Bleacher Report'}, 'author': 'NFL Staff',
             'title': "Bleacher Report's Expert NFL Conference Championship Picks & Predictions - Bleacher Report",
             'description': "For what it's worth, on each of the last four NFL Conference Championship Sundays, both favorites have either covered with impressive wins together or fallen short of expectations with close wins or losses together...",
             'url': 'https://bleacherreport.com/articles/2927682-bleacher-reports-expert-nfl-conference-championship-picks-predictions',
             'urlToImage': 'https://img.bleacherreport.net/img/slides/photos/004/434/332/03a0e00131dc411edfb8f017a74e8e24_crop_exact.jpg?w=1200&h=1200&q=75',
             'publishedAt': '2021-01-22T14:38:41Z',
             'content': 'Mark LoMoglio/Associated Press\r\nWhen: Sunday, 3:05 p.m. ET\r\nWhere: Lambeau Field, Green Bay\r\nTV: Fox\r\nReferee: Clete Blakeman\r\nLine:\xa0Green Bay -3.5\r\nFans in attendance:\xa0Approximately 6,500\r\nBuccaneer… [+1294 chars]'},
            {'source': {'id': None, 'name': 'Gizmodo.com'}, 'author': 'George Dvorsky',
             'title': "Here's What Biden Should Prioritize at NASA - Gizmodo",
             'description': 'We reached out to space experts, asking a very simple question: What should be Biden’s NASA priorities?',
             'url': 'https://gizmodo.com/heres-what-biden-should-prioritize-at-nasa-1846103628',
             'urlToImage': 'https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/qili6wpkqbdybdxtgdo9.jpg',
             'publishedAt': '2021-01-22T14:35:00Z',
             'content': 'Despite the ongoing pandemic, theres much to be excited about in space this year. NASAs Perseverance rover is less than a month away from landing on Mars; the James Webb Space Telescope is scheduled … [+9559 chars]'},
            {'source': {'id': None, 'name': 'CNBC'}, 'author': 'Todd Haselton',
             'title': 'Apple reportedly working on MacBooks with magnetic charging and new designs - CNBC',
             'description': "Apple will use its own processors instead of Intel's in the new Macs.",
             'url': 'https://www.cnbc.com/2021/01/22/apple-reportedly-working-on-thinner-lighter-macbook-air-with-magsafe.html',
             'urlToImage': 'https://image.cnbcfm.com/api/v1/image/106790480-1605032999840macbookair3-jpg?v=1605033066',
             'publishedAt': '2021-01-22T13:40:00Z',
             'content': 'Apple is planning to release a new thinner and lighter MacBook Air that will launch in the second half of this year or early next year, according to Bloomberg.\r\nThe report said Apple will plan to mar… [+1411 chars]'},
            {'source': {'id': 'fox-news', 'name': 'Fox News'}, 'author': 'Melissa Roberto',
             'title': "Ted Cruz slams 'rich' Seth Rogen after actor calls him a 'fascist' in spat over Biden's Paris climate pledge - Fox News",
             'description': "Sen. Ted Cruz, R-TX, and actor Seth Rogen duked it out on Twitter over one of President Biden's first executive orders.",
             'url': 'https://www.foxnews.com/entertainment/ted-cruz-slams-seth-rogen-actor-fascist-spat-biden-paris-climate-pledge',
             'urlToImage': 'https://static.foxnews.com/foxnews.com/content/uploads/2021/01/rogen-cruz.jpg',
             'publishedAt': '2021-01-22T13:28:29Z',
             'content': 'One of the several executive orders signed by President Biden during his first day in the White House resulted in a Twitter feud between Sen. Ted Cruz, R-TX, and actor Seth Rogen.\r\nRogen unleashed hi… [+3270 chars]'},
            {'source': {'id': None, 'name': 'New York Post'}, 'author': 'Noah Manskar',
             'title': 'Google threatens to shut off search engine in Australia over news law - New York Post ',
             'description': 'Google on Friday threatened to shut off its search engine in Australia if officials there approve a law requiring it to pay news publishers for their content. The Silicon Valley titan escalated its…',
             'url': 'https://nypost.com/2021/01/22/google-threatens-to-block-search-engine-in-australiagoogle-threatens-to-shut-off-search-engine-in-australia-over-news-law/',
             'urlToImage': 'https://nypost.com/wp-content/uploads/sites/2/2021/01/210122-google-australia-news1.jpg?quality=90&strip=all&w=1200',
             'publishedAt': '2021-01-22T13:19:00Z',
             'content': 'Google on Friday threatened to shut off its search engine in Australia if officials there approve a law requiring it to pay news publishers for their content.\r\nThe Silicon Valley titan escalated its … [+1873 chars]'},
            {'source': {'id': 'engadget', 'name': 'Engadget'}, 'author': '',
             'title': 'The Morning After: The Galaxy S21 reviews are in - Engadget',
             'description': 'The verdict is in for Samsung’s Galaxy S21 series. We’ve got two separate reviews for you today, one on the premium Ultra variant and another for the standard S21 — which should also inform you of what to expect from the S21+ model.',
             'url': 'https://www.engadget.com/galaxy-s21-review-tma-125048743.html',
             'urlToImage': 'https://o.aolcdn.com/images/dims?resize=1200%2C630&crop=1200%2C630%2C0%2C0&quality=95&image_uri=https%3A%2F%2Fs.yimg.com%2Fos%2Fcreatr-uploaded-images%2F2021-01%2F1ae24240-5caf-11eb-9af3-b9466ee5ac8e&client=amp-blogside-v2&signature=9f74fdae29f94111213e806346eb960d850dcb6c',
             'publishedAt': '2021-01-22T12:51:08Z',
             'content': 'The verdict is in for Samsung’s Galaxy S21 series. We’ve got two separate reviews for you today, one on the premium Ultra variant and another for the standard S21 — which should also inform you of wh… [+3012 chars]'},
            {'source': {'id': None, 'name': 'New York Post'}, 'author': 'Yaron Steinbuch',
             'title': "National Guardsmen allowed back into Capitol after being 'banished' to garage - New York Post ",
             'description': 'The National Guard troops who were “banished” to a cramped parking garage amid outrage after protecting Washington, DC, in the aftermath of the deadly riots have been allowed back into the US Capit…',
             'url': 'https://nypost.com/2021/01/22/national-guard-troops-allowed-in-capitol-after-being-moved-to-garage/',
             'urlToImage': 'https://nypost.com/wp-content/uploads/sites/2/2021/01/national-guard-66.jpg?quality=90&strip=all&w=1200',
             'publishedAt': '2021-01-22T12:51:00Z',
             'content': 'The National Guard troops who were banished to a cramped parking garage amid outrage after protecting Washington, DC, in the aftermath of the deadly riots have been allowed back into the US Capitol.\r… [+3405 chars]'},
            {'source': {'id': None, 'name': 'The Guardian'}, 'author': 'Jessica Glenza',
             'title': 'Biden team in race against time as new strain threatens to intensify Covid wave - The Guardian',
             'description': 'More infectious B117 variant adds to monumental scale of task as vaccine deployment called ‘a dismal failure so far’',
             'url': 'https://amp.theguardian.com/world/2021/jan/22/coronavirus-variant-biden-strategy-covid',
             'urlToImage': None, 'publishedAt': '2021-01-22T12:47:00Z',
             'content': 'Coronavirus<ul><li>More infectious B117 variant adds to monumental scale of task</li><li>Vaccine deployment called a dismal failure so far</li></ul>\r\nJoe Bidens new administration is faced with a mon… [+5238 chars]'},
            {'source': {'id': None, 'name': 'KXAN.com'}, 'author': 'The Associated Press, Nexstar Media Wire',
             'title': 'Dave Chappelle cancels shows after testing positive for COVID-19 - KXAN.com',
             'description': 'Dave Chappelle tested positive for the coronavirus just before his comedy show scheduled for Thursday, forcing his upcoming appearances to be canceled, a spokeswoman said.',
             'url': 'https://www.kxan.com/news/local/austin/dave-chappelle-cancels-shows-after-testing-positive-for-covid-19/',
             'urlToImage': 'https://www.kxan.com/wp-content/uploads/sites/40/2021/01/c1-1.jpg?w=1280',
             'publishedAt': '2021-01-22T12:46:00Z',
             'content': 'AUSTIN (AP) Dave Chappelle tested positive for the coronavirus just before his comedy show scheduled for Thursday, forcing his upcoming appearances to be canceled, a spokeswoman said.\r\nChappelle was … [+830 chars]'},
            {'source': {'id': None, 'name': 'CNBC'}, 'author': 'Matthew J. Belvedere',
             'title': '5 things to know before the stock market opens Friday - CNBC',
             'description': 'Dow futures fell Friday as Intel and IBM came under heavy pressure after releasing quarterly results late Thursday.',
             'url': 'https://www.cnbc.com/2021/01/22/5-things-to-know-before-the-stock-market-opens-january-22-2021.html',
             'urlToImage': 'https://image.cnbcfm.com/api/v1/image/106825470-1610740852681-NYSE-Photo-210115-PRESS-18.JPG?v=1610740932',
             'publishedAt': '2021-01-22T12:43:00Z',
             'content': 'Here are the most important news, trends and analysis that investors need to start their trading day:\r\n1. Dow set to drop on tech weakness, a day after strength in the sector\r\nTraders on the floor of… [+5042 chars]'}]}


class News(object):
    """Class holding a news search result"""
    def __init__(self, articles: List[Dict], title: str = 'Headlines'):
        self.articles = articles
        self.title = title

    def to_html(self):
        # return Styler.simple_html(self.articles)
        return Styler.advanced_html(self.articles, self.title)

    def to_html_to_file(self, path: Path):
        html_result = self.to_html()

        with path.open('w') as f:
            f.write(html_result)

    def to_json(self):
        return json.dumps(self.articles, indent=4)


class Client(object):
    """Talks to the API"""

    def __init__(self, api_key: str):
        self.api_key = f'&apiKey={api_key.strip()}'
        self.base_url = 'http://newsapi.org/v2'
        self.headlines = '/top-headlines?'
        self.everything = '/everything?'

    def _get_headlines(self, country_code: str):
        url = self.base_url + self.headlines + f'country={country_code}' + self.api_key
        resp = requests.get(str(url))
        data = resp.json()
        if data['status'] != 'ok':
            print(f'Issues retrieving headlines from [{country_code}] - status: [{data["status"]}]')
        return data

    def get_news(self) -> News:
        """Does not accept country code, nor combines them"""

        country = ['fr', 'us']

        # Get news headlines
        # PREVENTS CALLING THE API WHEN DEVELOPING
        if DEV:
            data = dummy_data
        else:
            data = self._get_headlines(country[1])

        return News(data['articles'], 'Headlines')

    def _kw_search(self, kw: List[str],) -> List[Dict]:
        url = self.base_url + self.everything + f'q={"+".join(kw)}' + self.api_key
        resp = requests.get(url)
        data = resp.json()
        if data['status'] != 'ok':
            print(f'Issues retrieving articles about [{kw}] - status: [{data["status"]}]')
        return data['articles']

    def search_keywords(self, kw: List[str], limit: int = 20) -> News:
        data = self._kw_search(kw)
        return News(data[:limit], f'Topic: [{", ".join(kw)}]')

    def tailored_news(self, limit: int = 20) -> News:
        data = []
        for kw in Interests.get_all():
            res = self._kw_search(kw)
            data.extend(res[:5])   # limiting to 5 article per topic
        random.shuffle(data)
        return News(data[:limit], 'Tailor')


if __name__ == "__main__":

    client = Client(get_key())

    data = client.get_news()
    print('HEADLINES')
    print(data.to_json())

    data = client.search_keywords(['blink', 'malcolm', 'gladwell'])
    print('SEARCH')
    print(data.to_json())
