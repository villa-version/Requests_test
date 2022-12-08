import requests
from bs4 import BeautifulSoup

channel = '@EgorLinch'
category = 'about'


def get_website(link):
    return requests.get(link)


def main(link_to_get_ws):
    response = get_website(link_to_get_ws)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        descr = soup.find('meta', {'name': 'description'})
        return descr.get('content')


if __name__ == '__main__':
    result = main("https://www.youtube.com/{channel}/{category}".format(channel=channel, category=category))
    print(result)

