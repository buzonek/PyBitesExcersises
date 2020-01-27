import re


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    result = []
    matches = re.search(r'(?P<start>.*)"(?P<middle>.*)"(?P<rest>.*)', text)
    matches.group('start') and result.extend(matches.group('start').split())
    matches.group('middle') and result.append(matches.group('middle'))
    matches.group('rest') and result.extend(matches.group('rest').split())
    return result
