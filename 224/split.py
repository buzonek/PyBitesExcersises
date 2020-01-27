import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    result = []
    text = re.sub('\n', ' ', text.strip())
    splitted_text = re.split(r'([!.?])(?=\s[A-Z]|$)', text)
    for line, punc in zip(splitted_text[0::2], splitted_text[1::2]):
        result.append(line.strip() + punc)
    return result


TEXT = """
PyBites was founded 19th of December 2016. That means that today,
14th of October 2019 we are 1029 days old. Time flies when you code
in Python. Anyways, good luck with this Bite. What is your favorite editor?
"""

print(get_sentences(TEXT))
