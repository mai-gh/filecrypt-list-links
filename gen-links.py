import requests
import sys
from time import sleep
from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'})
r = s.get(sys.argv[1])
soup = BeautifulSoup(r.text, 'html.parser')
buttons_list = soup.find_all(class_ = "download")
for b in buttons_list:
  first_link_code = b['onclick'].split("'")[1]
  first_link = "http://filecrypt.co/Link/" + first_link_code + '.html'
  first_link_resp = s.get(first_link)
  soup = BeautifulSoup(first_link_resp.text, 'html.parser')
  second_link = soup.find("script").text.split("'")[1]
  second_link_resp = s.get(second_link)
  print(second_link_resp.url)
  sleep(2)
