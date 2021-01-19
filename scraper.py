from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen
from collections import defaultdict


soccer_dict = defaultdict(list)

r = Request(
    "https://www.skysports.com/premier-league-results",
    headers={"User-Agent": "Mozilla/5.0"},
)
request_page = urlopen(r)
page_html = request_page.read()
request_page.close()
soup = bs(page_html, "html.parser")

# filename = "soccer.csv"
# f = open(filename, "W")


for games in soup.find_all("h4", class_="fixres__header2"):

    sibling = games.nextSibling
    while sibling is not None and sibling.name != "h4":
        if sibling.name == "div":
            soccer_dict[games.text].append(sibling)
        sibling = sibling.nextSibling

print(soccer_dict)
