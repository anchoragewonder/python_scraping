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


for games in soup.find_all("h4", class_="fixres__header2"):

    date = games.text
    sibling = games.nextSibling

    while sibling is not None and sibling.name != "h4":
        if sibling.name == "div":

            home_team = sibling.find("span", class_="matches__participant--side1")
            away_team = sibling.find("span", class_="matches__participant--side2")
            score = sibling.find_all("span", class_="matches__teamscores-side")

            homescore = score[0].text
            awayscore = score[1].text

            soccer_data["matches"].append(
                {
                    "date": games.text,
                    "team1": home_team.text,
                    "team2": away_team.text,
                    "score": [homescore, awayscore],
                }
            )
        sibling = sibling.nextSibling

print(json.dumps(soccer_data, indent=4))
