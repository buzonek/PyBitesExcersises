import re


def strip_comments(code):
    return re.sub(r'(^\s*"""[\w\W]*?"""\n)|(\s*# [\w\s]+?(?=\n))', '',
                  code, flags=re.MULTILINE)
