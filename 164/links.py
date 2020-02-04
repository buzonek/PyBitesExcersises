import sys

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin.readlines():
        if line.count(',') > 1 or 'http' not in line:
            continue
        href, name = line.split(',')
        # returns True if internal_link is in href
        if any([link in href for link in INTERNAL_LINKS]):
            target_tag = 'target="_blank'
        else:
            target_tag = ''
        print(f'<a href="{href.strip()}" {target_tag}>{name.strip()}</a>')


if __name__ == '__main__':
    make_html_links()
