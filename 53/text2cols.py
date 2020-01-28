from itertools import zip_longest
from textwrap import wrap

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    sections = text.split('\n\n')
    result = ''
    for row in zip_longest(*[wrap(section, COL_WIDTH) for section in sections],
                           fillvalue=''):
        result += '\t'.join(f'{col.strip():<{COL_WIDTH}}' for col in row)
        result += '\n'
    return result
