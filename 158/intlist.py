import statistics


class IntList(list):
    def __init__(self, values):
        super().__init__()
        self.values = values

    def __add__(self, other):
        self.append(other)
        return self.values

    def __iadd__(self, other):
        self.append(other)
        return self.values

    def append(self, other):
        if not isinstance(other, list):
            other = [other]
        for value in other:
            try:
                cast_value = int(value)
            except ValueError:
                raise TypeError
            else:
                self.values.append(cast_value)

    @property
    def median(self):
        return statistics.median(self.values)

    @property
    def mean(self):
        return statistics.mean(self.values)
