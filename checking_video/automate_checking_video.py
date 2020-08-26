from bs4 import BeautifulSoup
import requests

r=requests.get('https://www.youtube.com/user/FIFATV')
#print(r.text)
soup = BeautifulSoup(r.text, 'lxml')
print(soup.prettify())
