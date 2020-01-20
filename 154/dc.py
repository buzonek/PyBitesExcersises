from dataclasses import dataclass, field


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: str = 'Beginner'

    def __post_init__(self):
        self.title = f'{self.title[0].upper()}{self.title[1:]}'
