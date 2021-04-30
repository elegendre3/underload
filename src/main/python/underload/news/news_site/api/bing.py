import requests

url = "https://bing-news-search1.p.rapidapi.com/news"

querystring = {"safeSearch":"Off","textFormat":"Raw"}

headers = {
    'x-bingapis-sdk': "true",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "bing-news-search1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


# NEED FREEMIUM ACCOUNT -> Free up to 100 req/day