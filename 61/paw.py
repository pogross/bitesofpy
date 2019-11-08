from collections import namedtuple
import random
import string
from typing import List

ACTIONS = ["draw_card", "play_again", "interchange_cards", "change_turn_direction"]
NUMBERS = range(1, 5)

PawCard = namedtuple("PawCard", "card action")


def create_paw_deck(n: int = 8) -> List[PawCard]:
    if n > 26:
        raise ValueError

    letters = string.ascii_uppercase[:n]

    actions = random.choices(ACTIONS, k=n)  # 1/4 are actions
    actions.extend([None] * (n * 3))  # 3/4 are not actions
    random.shuffle(actions)

    cards = [
        PawCard(card=f"{letter}{number}", action=actions.pop())
        for letter in letters
        for number in NUMBERS
    ]

    return cards
