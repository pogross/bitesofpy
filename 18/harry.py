import os
import urllib.request
from collections import Counter
import re

# data provided
stopwords_file = os.path.join("tmp", "stopwords")
harry_text = os.path.join("tmp", "harry")
urllib.request.urlretrieve("http://bit.ly/2EuvyHB", stopwords_file)
urllib.request.urlretrieve("http://bit.ly/2C6RzuR", harry_text)


def get_harry_most_common_word():
    with open(stopwords_file, "r", encoding="utf-8") as sw:
        stopwords = sw.read().lower()

    with open(harry_text, "r", encoding="utf-8") as wf:
        raw_words = wf.read().lower().split()

    filtered_words = [re.sub(r"\W+", r"", word) for word in raw_words]
    word_list = [word for word in filtered_words if word not in stopwords]

    return Counter(word_list).most_common(1)[0]
