from collections import Counter
import re

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = "https://bites-data.s3.us-east-2.amazonaws.com/" "tribe-mentors-books.html"


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode("utf-8")


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()

    soup = BeautifulSoup(content, "html.parser")

    books = [
        (book["href"], book.text)
        for book in soup.findAll("a")
        if AMAZON in book["href"]
    ]

    top_books = Counter(books).most_common(limit)
    return [book[1] for book, _ in top_books]
