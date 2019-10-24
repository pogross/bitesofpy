from functools import wraps

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required(func):
    @wraps(func)
    def wrapper(user):
        if user in loggedin_users:
            return f"welcome back {user}"
        if user not in known_users:
            return "please create an account"
        return "please login"

    return wrapper


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    pass
