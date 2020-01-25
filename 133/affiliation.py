def generate_affiliation_link(url):
    splitted_url = url.split('/')
    return f'http://www.amazon.com/dp/{splitted_url[5]}/?tag=pyb0f-20'
