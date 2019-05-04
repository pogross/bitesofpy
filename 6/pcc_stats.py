"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request

# prep

tempfile = os.path.join("tmp", "dirnames")
urllib.request.urlretrieve("http://bit.ly/2ABUTjv", tempfile)

IGNORE = "static templates data pybites bbelderbos hobojoe1848".split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple("Stats", "user challenge")


#  code
def gen_files():
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile) as f:
        for line in f.read().splitlines():
            dir, is_dir = line.split(",")
            if is_dir == "True":
                yield dir


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    for dir in gen_files():
        challenge, user = dir.split("/")

        popular_challenges[challenge] += 1
        if user not in IGNORE:
            users[user] += 1

    top_user = users.most_common(1)[0][0]
    top_challenge = popular_challenges.most_common(1)[0]
    return Stats(user=top_user, challenge=top_challenge)


if __name__ == "__main__":
    print(diehard_pybites())
