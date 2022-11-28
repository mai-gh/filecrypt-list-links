import requests
import sys
from time import sleep
from bs4 import BeautifulSoup

# CONFIRMED BLOCKED USERAGENTS 
# 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'


# https://techblog.willshouse.com/2012/01/03/most-common-user-agents/
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'


s = requests.Session()
s.headers.update({'User-Agent': UA})
r = s.get(sys.argv[1])
soup = BeautifulSoup(r.text, 'html.parser')
buttons_list = soup.find_all(class_ = "download")
for b in buttons_list:
  first_link_code = b['onclick'].split("'")[1]
  first_link = "http://filecrypt.co/Link/" + first_link_code + '.html'
  first_link_resp = s.get(first_link)

  if first_link_resp.status_code == 404:
    print('ERROR 404: probably need to update User-Agent')
    exit()

  soup = BeautifulSoup(first_link_resp.text, 'html.parser')
  second_link = soup.find("script").text.split("'")[1]
  second_link_resp = s.get(second_link)
  print(second_link_resp.url)
  sleep(2)
