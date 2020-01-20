MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        def is_the_same(date, other):
            return date.day == other.day and date.month == other.month
        if any([x for x in self.values() if is_the_same(birthday, x)]):
            print(MSG.format(name))
        super(BirthdayDict, self).__setitem__(name, birthday)