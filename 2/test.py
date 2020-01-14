import re
COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')

regexp = "\d{2}:\d{2}"
print(re.findall(regexp, COURSE))


HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')

def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    regexp = '(?<=<p>).*?(?=</p>)'
    return re.findall(regexp, html)[0]

print(match_first_paragraph())