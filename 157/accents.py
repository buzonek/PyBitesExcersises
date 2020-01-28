from unicodedata import name


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return [x.lower() for x in text if 'WITH' in name(x)]
