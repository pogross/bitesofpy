import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    users = {}
    for entry in passwd.strip().splitlines():
        split = entry.split(":")
        account = split[0]

        if split[4]:
            users[account] = re.sub(",+", " ", split[4]).strip()
        else:
            users[account] = "unknown"

    return users

