class Animal:

    index = 10001
    animals = list()

    def __init__(self, name):
        self.name = f'{Animal.index}. {name.title()}'
        Animal.index += 1
        Animal.animals.append(self)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def zoo(cls):
        return [str(animal) for animal in cls.animals]