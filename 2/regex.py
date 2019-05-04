import re


def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = (
        "Introduction 1 Lecture 01:47"
        "The Basics 4 Lectures 32:03"
        "Getting Technical!  4 Lectures 41:51"
        "Challenge 2 Lectures 27:48"
        "Afterword 1 Lecture 05:02"
    )
    course_times = re.findall(r"\d{2}:\d{2}", flask_course)
    return course_times


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = (
        "New PyBites article: Module of the Week - Requests-cache "
        "for Repeated API Calls - http://pybit.es/requests-cache.html "
        "#python #APIs"
    )
    urls = re.findall(r"http.*html", tweet)
    hashtags = re.findall(r"\B(\#[a-zA-Z]+\b)(?!;)", tweet)
    return urls + hashtags


def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = "<p>pybites != greedy</p>" "<p>not the same can be said REgarding ...</p>"
    return re.findall(r"(?<=<p>)(.*?)(?=<\/p>)", html)[0]


if __name__ == "__main__":
    print(extract_course_times())
    print(get_all_hashtags_and_links())
    print(match_first_paragraph())
