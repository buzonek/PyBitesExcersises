from functools import total_ordering


@total_ordering
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []
        self.index = 0

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self) - 1:
            raise StopIteration
        value = self._transactions[self.index]
        self.index += 1
        return value

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError
        self._transactions.append(other)

    def __sub__(self, other):
        if not isinstance(other, int):
            raise ValueError
        self._transactions.append(-other)

    def __str__(self):
        return f'{self.name} account - balance: {self.balance}'

    def __getitem__(self, item):
        return self._transactions[item]