import requests
from bs4 import BeautifulSoup


def retrieve_url(url: str) -> str:
    params = {
        'url': url
    }
    response = requests.get('http://archive.org/wayback/available', params=params)
    data = response.json()
    if len(data['archived_snapshots']) > 0:
        return data['archived_snapshots']['closest']['url']
    else:
        return 'not_found'

def parse(url: str) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    wayback_menu = soup.find(id="wm-ipp-base")
    if wayback_menu:
        wayback_menu.decompose()
    return str(soup)
