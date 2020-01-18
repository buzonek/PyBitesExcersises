import re
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    all_reboots = re.findall(r'[\w ]+\d+ [\d:]+', reboots)
    dt_reboots = [parse(x.strip()) for x in all_reboots]

    longest_uptime = 0
    reboot = None
    for d1, d2 in zip(dt_reboots, dt_reboots[1:]):
        delta = (d1 - d2).days
        if delta > longest_uptime:
            longest_uptime = delta
            reboot = d1
    return longest_uptime, str(reboot.date() - relativedelta(years=1))