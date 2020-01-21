class Person(object):
    msg = "I am a person"

    def __repr__(self):
        return self.msg


class Mother(Person):
    def __init__(self):
        self.msg = super().msg + " and awesome mom"


class Father(Person):
    def __init__(self):
        self.msg = super().msg + " and cool daddy"


class Child(Father, Mother):
    def __init__(self):
        self.msg = "I am the coolest kid"

    def __repr__(self):
        return self.msg