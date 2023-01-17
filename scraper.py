from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req

link = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["name", "distance", "mass", "radius"]

webpage = req.get(link, verify=False)

soup = bs(webpage.text, "html.parser")

data = []

star_table = soup.find_all("table")

table_rows = star_table.find_all('tr')

for i in table_rows:
    td = i.find_all('td')
    row = [i.text.rstrip() for j in i]

    data.append(row)


starName = list()
radius = list()
mass = list()
distance = list()

for i in range(1, len(data)):
    starName.append(data[i][1])
    distance.append(data[i][3])
    mass.append(data[i][5])
    radius.append(data[i][6])

star_df = pd.DataFrame(data, columns=headers)

star_df.to_csv('scraped_data.csv',index=True, index_label="id")
