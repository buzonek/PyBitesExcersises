import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """
    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper(), None)

    @staticmethod
    def hex2rgb(hex_):
        """Class method that converts a hex value into an rgb one"""
        if not hex_.startswith('#') or len(hex_) < 7:
            raise ValueError
        rgb = (hex_[1:3], hex_[3:5], hex_[5:7])
        return tuple(int(x, 16) for x in rgb)

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if any(x for x in rgb if x not in range(0, 256)):
            raise ValueError
        return f'#{"".join(hex(x).split("x")[1].rjust(2, "0") for x in rgb)}'

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f'{self.rgb}' if self.rgb else 'Unknown'
