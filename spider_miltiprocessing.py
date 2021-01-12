from multiprocessing import pool
import bs4 as bs
import random
import requests
import string


def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(
        string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url


def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link


def get_links(url):
    resp = requests.get(url)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    body = soup.body
    links = [link.get('href') for link in body.find_all('a')]
    links = [handle_local_links(url, link) for link in links]
    links = [str(link.encode("ascii")) for link in links]
    return links


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        print(e)
        print('Got a TypeError, probably got a None that we tried to iterate over')
        return []
    except IndexError as e:
        print(e)
        print('We probably did not find any useful links, returning empty list')
        return []
    except AttributeError as e:
        print(e)
        print('Likely got None for links, so we are throwing this')
        return []
    except Exception as e:
        print(str(e))
        # log this error
        return []
