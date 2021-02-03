from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from datetime import datetime
import json
import re

# creation of json object with matches as an index entry
soccer_data = {}
soccer_data["matches"] = []

# requesting the url to scrape from
r = Request(
    "https://www.skysports.com/premier-league-results",
    headers={"User-Agent": "Mozilla/5.0"},
)

# telling beutiful soup what to scrape and acces as the soup object
request_page = urlopen(r)
page_html = request_page.read()
request_page.close()
soup = bs(page_html, "html.parser")

# finding the html that contains the month/year and itterating over every instance of it
# for each month we are finding the sibling html that contains date info for each game
for games in soup.find_all("h3", class_="fixres__header1"):

    year = games.text

    # this sibling contains day info ex: Tuesday 4th January
    sibling = games.find_next_sibling("h4")
    sibling2 = sibling.nextSibling
    month = sibling.text

    # regex to strip the day name ex: Monday and the trailing sting ex: 14th or 2nd ---to--- 14 or 2
    month_simple = re.findall("\d+", month)
    month_simple = f"{month_simple[0]:0>2}"

    # we want to itterate over the following sibling because  h3, h4 and div classes are all siblings not nested
    # itterattion h3-->h4---> div---> while not h3 if ==div do x else if == h4  update h4 values stored as month
    while sibling2 is not None and sibling2.name != "h3":
        if sibling2.name == "div":

            home_team = sibling2.find("span", class_="matches__participant--side1")
            home_team = re.sub("\s+", "", home_team.text).strip()
            away_team = sibling2.find("span", class_="matches__participant--side2")
            away_team = re.sub("\s+", "", away_team.text).strip()

            score = sibling2.find_all("span", class_="matches__teamscores-side")
            home_score = int(re.sub("\s+", "", score[0].text).strip())
            away_score = int(re.sub("\s+", "", score[1].text).strip())

            # concatentaing string of the simplified mont and year objects  2 + 10 2020
            # and conversion to date time object then back to proper datetime string
            # 2 10 2020 00:00 ---> to 10/02/2020
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
