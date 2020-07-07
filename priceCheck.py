import requests
import time
from bs4 import BeautifulSoup

# TestURL = 'https://geizhals.at/sony-wf-1000xm3-schwarz-wf1000xm3b-ce7-a2089846.html'
print('give me a geizhals product link')
URL = input()

print('how often do you wanna check? input in seconds ')
sleeptime = int(input())


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}


def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h1", {"class": "variant__header__headline"}).getText()
    price = soup.find("span", {"class": "gh_price"}).getText()
    print(f'{title} \n PREIS: {price}')


x = 0
while True:
    x += 1
    print(x)
    checkPrice()
    time.sleep(sleeptime)
