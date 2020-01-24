from collections import namedtuple
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Set

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


@dataclass
class User:
    name: str
    _transactions: List = field(default_factory=list)
    _fans: Set = field(default_factory=set)

    def __add__(self, other):
        self._transactions.append(other.points)
        self._fans.add(other.giver)

    @property
    def karma(self):
        return sum(self._transactions)

    @property
    def fans(self):
        return len(self._fans)

    @property
    def points(self):
        return self._transactions

    def __str__(self):
        fan = 'fan' if self.fans < 2 else 'fans'
        return f'{self.name} has a karma of {self.karma} and {self.fans} {fan}'
