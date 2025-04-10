import requests
from bs4 import BeautifulSoup

def scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.get_text()

url = "https://guthib.com/"
webpage_text = scraper(url)
print(webpage_text)