from pytz import timezone, utc
from datetime import datetime

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt: datetime):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aware = utc.localize(naive_utc_dt)
    return aware.astimezone(AUSTRALIA), aware.astimezone(SPAIN)
