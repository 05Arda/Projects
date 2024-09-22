import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Comparison_of_programming_languages'
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

csv = pd.DataFrame(columns=rows[0].text.strip().split('\n\n'))

for i in range(1, len(rows)):
    csv.loc[i-1] = rows[i].text.strip().split('\n\n')

csv.to_csv('language.csv', index=False)

a = pd.read_csv("language.csv")
print(a.head())