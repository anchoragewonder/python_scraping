from bs4 import BeautifulSoup
from urllib.request import urlopen

url_to_scrape = "https://www.google.com/search?q=premier+leage+scores&rlz=1C1ASUM_enUS865US865&oq=premier+leage+scores&aqs=chrome..69i57j0i10i131i433i457j0i10j0i10i395l7.8842j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/g/11j4y8fvpd;2;/m/02_tc;mt;fp;1;;"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

soccer_items = html_soup.find _all('div', class_="OcbAbf")

filename = 'soccer.json'
f = open(filenmane, 'W')


for games in soccer_items
    matchday = game.find('div', class_="imspo_mt_cmd")

    f.write(matchday + ': {')