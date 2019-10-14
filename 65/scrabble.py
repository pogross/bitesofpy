from typing import List, Set
import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join("tmp", "dictionary.txt")
urllib.request.urlretrieve("http://bit.ly/2iQ3dlZ", DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = {word.strip().lower() for word in f.read().split()}


def get_possible_dict_words(draw: List[str]) -> Set[str]:
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    return {word for word in _get_permutations_draw(draw) if word in dictionary}


def _get_permutations_draw(draw: List[str]) -> Set[str]:
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    return {
        "".join(x).lower()
        for l in range(1, len(draw))
        for x in itertools.permutations(draw, l)
    }
