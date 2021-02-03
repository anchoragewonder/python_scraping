from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
import json

soccer_data = {}
soccer_data["matches"] = []


r = Request(
    "https://www.skysports.com/premier-league-results",
    headers={"User-Agent": "Mozilla/5.0"},
)
request_page = urlopen(r)
page_html = request_page.read()
request_page.close()
soup = bs(page_html, "html.parser")

# filename = "soccer.txt"
# f = open(filename, "W")


for games in soup.find_all("h3", class_="fixres__header1"):

    year = games.text
    sibling = games.find_next_sibling("h4")
    sibling2 = sibling.nextSibling
    month = sibling.text

    while sibling2 is not None and sibling2.name != "h3":
        if sibling2.name == "div":

            home_team = sibling2.find("span", class_="matches__participant--side1")
            away_team = sibling2.find("span", class_="matches__participant--side2")
            score = sibling2.find_all("span", class_="matches__teamscores-side")

            home_score = score[0].text
            away_score = score[1].text

            soccer_data["matches"].append(
                {
                    "date": month + year,
                    "homeTeam": home_team.text,
                    "awayTeam": away_team.text,
                    "homeScore": home_score,
                    "awayScore": away_score,
                }
            )
        elif sibling2.name == "h4":
            month = sibling2.text
        sibling2 = sibling2.nextSibling

print(json.dumps(soccer_data, indent=4))
