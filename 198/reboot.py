from itertools import tee
from datetime import datetime
import re

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def calc_max_uptime(reboots: str = MAC1) -> tuple:
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    reboot_times = re.findall(r"(?=[A-Z])(.*)(?![:1-9])", reboots)
    reboot_dt = [datetime.strptime(f"{datetime.now().year} {reboot}", "%Y %a %b %d %H:%M") for reboot in reboot_times]

    reboot_deltas = {}
    for curr_dt, next_dt in pairwise(reboot_dt):
        reboot_deltas[curr_dt - next_dt] = curr_dt

    max_up = max(reboot_deltas)
    return max_up.days, str(reboot_deltas[max_up].date())
