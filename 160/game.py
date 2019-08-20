import csv
import os
from collections import defaultdict
from typing import Dict, List
from urllib.request import urlretrieve

BATTLE_DATA = os.path.join("tmp", "battle-table.csv")
if not os.path.isfile(BATTLE_DATA):
    urlretrieve("https://bit.ly/2U3oHft", BATTLE_DATA)


def _create_defeat_mapping() -> Dict[str, List[str]]:
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    with open(BATTLE_DATA) as f:
        data = f.readlines()

    targets = data[0].strip().split(",")
    outcomes = data[1:]

    defeat_mapping = defaultdict(list)
    for line in outcomes:
        attacks = line.strip().split(",")
        attacker = attacks[0]
        for result, target in zip(attacks, targets):
            if result == "win":
                defeat_mapping[attacker].append(target)

    return defeat_mapping


def get_winner(player1: str, player2: str, defeat_mapping: dict = None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()

    if player1 not in defeat_mapping.keys() or player2 not in defeat_mapping.keys():
        raise ValueError("These moves are not valid!")

    if player1 == player2:
        return "Tie"

    if player2 in defeat_mapping[player1]:
        return player1
    else:
        return player2
