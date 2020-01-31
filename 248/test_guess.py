from unittest.mock import patch

import pytest

from guess import GuessGame, InvalidNumber


def test_default_value():
    game = GuessGame(1)
    assert game.secret_number == 1
    assert game.max_guesses == 5


def test_raises_not_int():
    with pytest.raises(InvalidNumber) as excinfo:
        GuessGame('test')
    assert 'Not a number' in str(excinfo.value)


def test_raises_negative():
    with pytest.raises(InvalidNumber) as excinfo:
        GuessGame(-2)
    assert 'Negative number' in str(excinfo.value)


def test_raises_too_high():
    with pytest.raises(InvalidNumber) as excinfo:
        GuessGame(16)
    assert 'Number too high' in str(excinfo.value)


@patch('builtins.input', side_effect=['test', -1, 16, 12])
def test_prompt(mock, capfd):
    game = GuessGame(12)
    game()
    output = capfd.readouterr()[0]
    assert "Guess a number: " in output
    assert "Enter a number, try again" in output
    assert "Too low" in output
    assert "Too high" in output
    assert "You guessed it!" in output
    assert game.attempt == 3


@patch('builtins.input', side_effect=[1, 1, 1, 1, 1, 1, 1])
def test_too_many_attemts(mock, capfd):
    game = GuessGame(12)
    game()
    output = capfd.readouterr()[0]
    assert "Sorry, the number was 12" in output
    assert game.attempt == game.max_guesses
