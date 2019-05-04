from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    """Raised when user does not exist"""

    pass


class UserAccessExpired(Exception):
    """Raised when user access has expired"""

    pass


class UserNoPermission(Exception):
    """Raised when user has no permission"""

    pass


def get_secret_token(username):

    user = [user for user in USERS if user.name == username]
    if len(user) == 0:
        raise UserDoesNotExist
    if user[0].expired:
        raise UserAccessExpired
    if user[0].role != ADMIN:
        raise UserNoPermission

    return SECRET
