from pathlib import PosixPath
import os
import difflib


def get_matching_files(directory: PosixPath, filter_str: str) -> list:
    """Get all file names in "directory" and (case insensitive) match the ones
       that exactly match "filter_str"

       In case there is no exact match, return closely matching files.
       If there are no closely matching files either, return an empty list.
       (Return file names, not full paths).

       For example:

       d = Path('.')
       files in dir: bite1 test output

       get_matching_files(d, 'bite1') => ['bite1']
       get_matching_files(d, 'Bite') => ['bite1']
       get_matching_files(d, 'pybites') => ['bite1']
       get_matching_files(d, 'test') => ['test']
       get_matching_files(d, 'test2') => ['test']
       get_matching_files(d, 'output') => ['output']
       get_matching_files(d, 'o$tput') => ['output']
       get_matching_files(d, 'nonsense') => []
    """
    filter_words = filter_str.split()
    files = [fname.lower() for fname in os.listdir(directory)]

    matched_files = [fname for fname in files if fname in filter_words]
    if matched_files:
        return matched_files

    close_matches = [
        match
        for word in filter_words
        for match in difflib.get_close_matches(word, files)
    ]

    return close_matches if close_matches else []
