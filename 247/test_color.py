from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


def test_gen_hex_color_3(gen):
    assert len(next(gen)) == 7


def test_gen_hex_color(gen):
    with patch.object(color, 'sample') as mock_obj:
        mock_obj.return_value = (0, 0, 0)
        assert next(gen) == "#000000"


def test_gen_hex_color_4(gen):
    with patch.object(color, 'sample') as mock_obj:
        mock_obj.return_value = (0, 0, 0)
        next(gen)
        sequence = list(mock_obj.call_args[0][0])
        count = mock_obj.call_args[0][1]
        for arg in sequence:
            assert arg in range(0, 256)
        assert count == 3
