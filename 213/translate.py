import re


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    tags_org = re.findall(r'<code>.*?<\/code>|<pre>[\w\s\W]*?<\/pre>', org_text)
    tags_trns = re.findall(r'<code>.*?<\/code>|<pre>[\w\s\W]*?<\/pre>',
                           trans_text)
    for tag_org, tag_trns in zip(tags_org, tags_trns):
        trans_text = trans_text.replace(tag_trns, tag_org)
    return trans_text
