import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'

VIEWS_LIMIT = 1000000


def load_data(url):
    return requests.get(url).content.decode('utf-8')


def top_python_questions(url=cached_so_url):
    soup = BeautifulSoup(load_data(url), 'html.parser')
    questions = soup.find_all('div', {'class': 'question-summary'})
    top_questions = []
    for question in questions:
        views_div = question.find('div', {'class': 'views'})
        views = int(views_div['title'].replace(',', '').split()[0])
        if views > VIEWS_LIMIT:
            vote_div = question.find("div", {'class': 'vote'})
            votes = int(vote_div.span.text)
            question_a = question.find('a', {'class': 'question-hyperlink'})
            question_str = question_a.text
            top_questions.append((question_str, votes))
    return sorted(top_questions, key=lambda x: x[1], reverse=True)
