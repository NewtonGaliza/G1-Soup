import requests
from bs4 import BeautifulSoup

page = requests.get('http://g1.globo.com/pb/paraiba')

soup = BeautifulSoup(page.content, 'html.parser')

footer = soup.find('footer')
footer.decompose()

listheadlines = soup.find_all('a', class_='feed-post-link')

for headline in listheadlines:
    print(headline.get_text())
