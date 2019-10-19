import re
from collections import Counter
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path("tmp")
PYCON_HTML = TMP / "pycon2019.html"
if not PYCON_HTML.exists():
    urlretrieve("https://bit.ly/2O5Bik7", PYCON_HTML)


def _get_soup(html: Path = PYCON_HTML) -> Soup:
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup: Soup = _get_soup()) -> List[str]:
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    raw_speakers = [
        entry.text.strip() for entry in soup.findAll("span", {"class": "speaker"})
    ]
    speakers = [
        speaker.strip()
        for speakers in raw_speakers
        for speaker in re.split(r"[\,/]", speakers)
    ]
    return [name.split()[0] for name in speakers]


def get_percentage_of_female_speakers(first_names: list) -> float:
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places."""
    d = gender.Detector(case_sensitive=False)
    count = Counter([d.get_gender(name) for name in first_names])
    female_percantage = (
        (count["female"] + count["mostly_female"]) / len(first_names) * 100
    )

    return round(female_percantage, 2)


if __name__ == "__main__":
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
