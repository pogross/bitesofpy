from collections import namedtuple
import requests
from bs4 import BeautifulSoup

cached_so_url = "https://bit.ly/2IMrXdp"

Question = namedtuple("Question", ["text", "votes", "views"])


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(url)

    soup = BeautifulSoup(markup=r.text, features="html.parser")

    questions = []
    for summary in soup.findAll("div", {"class": "question-summary"}):
        text = summary.findAll("a", {"class": "question-hyperlink"})[0].text.strip()
        votes = summary.findAll("span", {"class": "vote-count-post"})[0].text.strip()
        views = (
            summary.findAll("div", {"class": "views"})[0]
            .text.strip()
            .replace(" views", "")
        )
        questions.append(Question(text, votes, views))

    filtered_questions = [
        (question.text, int(question.votes))
        for question in questions
        if "m" in question.views
    ]
    return sorted(filtered_questions, key=lambda x: x[1], reverse=True)
