import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')
print(website_ranking[:6])
html_website_ranking_address = [website_ranking_element.get_text() for website_ranking_element in website_ranking[1:]]

print("[Top Sites in South Korea]")
for k in range(6):
    print("{0}: {1}".format(k+1, html_website_ranking_address[k]))


website_ranking_dict = {'Website':html_website_ranking_address}
df = pd.DataFrame(website_ranking_dict, columns=['Website'], index=range(1, len(html_website_ranking_address)+1))
print(df[0:6])