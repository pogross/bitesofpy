import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Union
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

out_dir = "tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


class Enchantment:
    """Minecraft enchantment class

    Implements the following:
        id_name, name, max_level, description, items
    """

    id_name: str
    name: str
    max_level: Union[int, str]
    description: str
    items: List[str]

    def __init__(
        self, id_name=None, name=None, max_level=None, description=None, items=None
    ):
        self.id_name = id_name
        self.name = name
        self.max_level = (
            max_level if isinstance(max_level, int) else roman_to_int(max_level)
        )
        self.description = description

        if not items:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"


class Item:
    """Minecraft enchantable item class

    Implements the following:
        name, enchantments
    """

    name: str
    enchantments: List[Enchantment]

    def __init__(self, name=None, enchantments=None):
        self.name = name

        if not enchantments:
            self.enchantments = []
        else:
            self.enchantments = enchantments

    def __str__(self):
        name = f"{self.name.replace('_', ' ').title()}: \n"
        enchs = "\n".join(
            f"  [{enchantment.max_level}] {enchantment.id_name}"
            for enchantment in sorted(self.enchantments, key=lambda x: x.id_name)
        )
        return name + enchs.rstrip("\n")


# Source: https://codereview.stackexchange.com/questions/68297/convert-roman-to-int
def roman_to_int(
    roman, values={"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
):
    """Convert from Roman numerals to an integer."""
    numbers = []
    for char in roman:
        numbers.append(values[char])
    total = 0
    num2 = numbers[0]
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 >= num2:
            total += num1
        else:
            total -= num1
    return total + num2


def generate_enchantments(soup: Soup) -> Dict[str, Enchantment]:
    """Generates a dictionary of Enchantment objects

    With the key being the id_name of the enchantment.
    """
    enchantments = dict()

    table = soup.find("table", attrs={"id": "minecraft_items"})
    rows = table.find_all("tr")

    for row in rows[1:]:
        cells = row.find_all("td")

        id_name = cells[0].em.text.strip()
        name = cells[0].a.text.strip()
        max_level = cells[1].text.strip()
        description = cells[2].text.strip()

        items_raw = re.search(r"images\/(.*)\.png", cells[4].img.get("data-src")).group(
            1
        )
        items_clean = (
            items_raw.replace("enchanted", "")
            .replace("iron", "")
            .replace("sm", "")
            .replace("rod", "")
            .strip()
        )
        items = [
            item if "fishing" not in item else "fishing_rod"
            for item in items_clean.split("_")
            if item is not ""
        ]

        enchantments[id_name] = Enchantment(
            id_name, name, max_level, description, items
        )

    return enchantments


def generate_items(data: dict) -> Dict[str, Item]:
    """Generates a dictionary of Item objects

    With the key being the item name.
    """
    items = dict()

    for item in sorted(
        list({item for enchantment in data.values() for item in enchantment.items})
    ):
        item_enchantments = [
            enchantment for enchantment in data.values() if item in enchantment.items
        ]
        items[item] = Item(item, item_enchantments)

    return items


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.

    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor:
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns

Axe:
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite

Boots:
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker

Bow:
  [1] flame
  [1] infinity
  [5] power
  [2] punch

Chestplate:
  [1] mending
  [3] unbreaking
  [1] vanishing_curse

Crossbow:
  [1] multishot
  [4] piercing
  [3] quick_charge

Fishing Rod:
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse

Helmet:
  [1] aqua_affinity
  [3] respiration

Pickaxe:
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse

Shovel:
  [5] efficiency
  [3] fortune
  [1] silk_touch

Sword:
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse

Trident:
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
