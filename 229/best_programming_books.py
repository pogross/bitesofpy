from dataclasses import dataclass
from typing import List
from itertools import islice
import operator
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

url = "https://bites-data.s3.us-east-2.amazonaws.com/" "best-programming-books.html"
tmp = Path("tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)


@dataclass
class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """

    title: str
    author: str
    year: int
    rank: int
    rating: float

    def __post_init__(self):
        self.rating = float(self.rating)

    def update_rank(self, books) -> None:
        rank = books.index(self) + 1
        self.rank = rank

    def __str__(self):
        return f"[{self.rank:03d}] {self.title} ({self.year})\n{' '*6}{self.author} {self.rating}"


def _get_soup(file: Path) -> BeautifulSoup:
    return BeautifulSoup(file.read_text(encoding="utf-8"), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    if limit > len(books):
        limit = len(books)

    if year:
        filtered = [book for book in books if book.year >= year]
    else:
        filtered = books

    for book in islice(filtered, limit):
        print(book)


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)
    books_soup = soup.findAll("div", attrs={"class": "book accepted normal"})

    books = []
    for book in books_soup:

        title = book.findAll("a", attrs={"class": "book-title"})[0].h2.text
        if "python" not in title.lower():
            continue

        author_raw = book.findAll("h3", attrs={"class": "authors"})[0].a.text
        author_parts = author_raw.split(" ")
        author = f"{author_parts[-1]}, {' '.join(author_parts[:-1])}"

        year = book.findAll("span", attrs={"class": "date"})
        if not year:
            continue
        else:
            year = int(year[0].text.strip(" | "))

        rating = float(book.findAll("span", attrs={"class": "our-rating"})[0].text)

        books.append(Book(title=title, author=author, year=year, rank=0, rating=rating))

    books = sorted(
        books,
        key=lambda x: (-x.rating, x.year, x.title.lower(), x.author.split(",")[0], x.title),
    )
    for book in books:
        book.update_rank(books)

    return books


def main():
    books = load_data()
    display_books(books, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""
