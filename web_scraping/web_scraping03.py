import requests
from bs4 import BeautifulSoup

# url = "http://music.naver.com/listen/history/index.nhn?type=TOTAL&year=2017&month=12&week=1"
url = "https://music.naver.com/listen/history/index.nhn?type=TOTAL_V2&year=2019&month=10&week=0"
html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

# a 태그의 요소 중에서 class 속성값이 "_title" 인 것을 찾고
# 그 안에서 span 태그의 요소 중에서 class 속성값이 "ellipsis"인 요소를 추출
titles = soup_music.select('a._title span.ellipsis')
music_titles = [title.get_text() for title in titles]
print(music_titles[0:7])

artists = soup_music.select('a._artist span.ellipsis')
print(artists[0].get_text().strip())
music_artists = [artist.get_text().strip() for artist in artists]
print(music_artists[0:12])

artists = soup_music.select('td._artist a')
print(artists[0].get_text().strip())
music_artists = [artist.get_text().strip() for artist in artists]
print(music_artists[0:12])
