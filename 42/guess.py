import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        self._guesses = []
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        user_input = input(f"Guess a number between {START} and {END}")
        if not user_input:
            raise ValueError('Please enter a number')
        try:
            guess = int(user_input)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END + 1):
            raise ValueError('Number not in range')
        elif guess in self._guesses:
            raise ValueError('Already guessed')
        self._guesses.append(guess)
        return guess

    def _validate_guess(self, guess):
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        if guess > self._answer:
            print(f'{guess} is too high')
        else:
            print(f'{guess} is too low')
        return False

    def __call__(self):
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as error:
                print(error)
            if self._validate_guess(guess):
                print(f'It took you {len(self._guesses)} guesses')
                self._win = True
                return
        else:
            print(f'Guessed {len(self._guesses)} times,'
                  f' answer was {self._answer}')


if __name__ == '__main__':
    game = Game()
    game()
