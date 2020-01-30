from collections import namedtuple

import requests
from bs4 import BeautifulSoup as Soup

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')

    div = soup.find('div', 'dotd-main-book-summary')

    """ Part to extract the title"""
    title = div.contents[3].h2.text.strip()

    """Part to extract the description"""
    desc = div.contents[7].get_text().strip()

    dotd_div = soup.find('div', 'dotd-main-book-image')

    """Part to extract the link"""
    link = dotd_div.a['href']

    """Part to extract the image"""
    image = dotd_div.a.img['src']

    return Book(title, desc, image, link)
