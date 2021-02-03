from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from datetime import datetime
import json
import re

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
    month_simple = re.findall("\d+", month)
    month_simple = f"{month_simple[0]:0>2}"

    while sibling2 is not None and sibling2.name != "h3":
        if sibling2.name == "div":

            home_team = sibling2.find("span", class_="matches__participant--side1")
            home_team = re.sub("\s+", "", home_team.text).strip()
            away_team = sibling2.find("span", class_="matches__participant--side2")
            away_team = re.sub("\s+", "", away_team.text).strip()

            score = sibling2.find_all("span", class_="matches__teamscores-side")
            home_score = int(re.sub("\s+", "", score[0].text).strip())
            away_score = int(re.sub("\s+", "", score[1].text).strip())

            date_object = month_simple + " " + year

            new_date_object = datetime.strptime(date_object, "%d %B %Y")
            formatted_date = new_date_object.strftime("%m/%d/%Y")

            soccer_data["matches"].append(
                {
                    "date": formatted_date,
                    "homeTeam": home_team,
                    "awayTeam": away_team,
                    "homeScore": home_score,
                    "awayScore": away_score,
                }
            )
        elif sibling2.name == "h4":
            month = sibling2.text
            month_simple = re.findall("\d+", month)
            month_simple = f"{month_simple[0]:0>2}"
        sibling2 = sibling2.nextSibling

print(json.dumps(soccer_data, indent=4))
