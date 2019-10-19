from collections import namedtuple

import requests
from bs4 import BeautifulSoup as Soup

CONTENT = requests.get("http://bit.ly/2EN2Ntv").text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")

    title = soup.find("div", attrs={"class": "dotd-title"}).text.strip()
    description = (
        soup.find("div", attrs={"class": "dotd-main-book-summary"})
        .contents[7]
        .text.strip()
    )
    img_link = soup.find("div", attrs={"class": "dotd-main-book-image"})
    img = img_link.img["src"].strip()
    link = img_link.a["href"].strip()

    return Book(title, description, img, link)
