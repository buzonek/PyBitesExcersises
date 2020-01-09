# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    validators = dict()
    pattern = r'(?P<platform>\w+)\n\s+Min: (?P<Min>\d+)\n\s+Max:\s+(?P<Max>\d+)\n\s+.*:\s(?P<regexp>.*)'
    matches = re.finditer(pattern, social_platforms)
    for match in matches:
        platform = match.group('platform')
        min_ = int(match.group('Min'))
        max_ = int(match.group('Max'))
        regexp = match.group('regexp')
        validators[platform] = Validator(range(min_, max_ + 1), re.compile('^[' + re.sub(' ', '', regexp) + ']+$'))
    return validators


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    validator = all_validators.get(platform)
    if not validator:
        raise ValueError
    if len(username) in validator.range and validator.regex.match(username):
        return True
    return False
