from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime = NOW):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return datetime.now() > self.expires
