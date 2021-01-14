from bs4 import BeautifulSoup
from urllib.request import urlopen

url_to_scrape = "https://www.google.com/search?q=premier+leage+scores&rlz=1C1ASUM_enUS865US865&oq=premier+leage+scores&aqs=chrome..69i57j0i10i131i433i457j0i10j0i10i395l7.8842j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/g/11j4y8fvpd;2;/m/02_tc;mt;fp;1;;"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

soccer_items = html_soup.find_all('div', class_="OcbAbf")

filename = 'soccer.csv'
f = open(filenmane, 'W')


for games in soccer_items
    game_table = games.find_all('table', class_="KAIX8d")

    for data in game_table
        matchday = data.find('div', class_="imspo_mt_cmd").span
        team_row = data.find_all('tr', class_="L5Kkcd")
        home_team_row = team_row[0]
        away_team_row = team_row[1]

        for teams in team_row

