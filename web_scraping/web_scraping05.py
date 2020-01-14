import glob

import requests
from bs4 import BeautifulSoup

naver_music_url = "https://music.naver.com/listen/history/index.nhn?type=TOTAL_V2&year=2019&month=10&week=0"


# 네이버 music 주소를 입력하면 노래 제목과 아티스트를 반환
def naver_music(url):
    html_music = requests.get(url).text
    soup_music = BeautifulSoup(html_music, "lxml")

    titles = soup_music.select('a._title span.ellipsis')
    artists = soup_music.select('td._artist a')

    music_titles = [title.get_text() for title in titles]
    music_artists = [artist.get_text().strip() for artist in artists]

    return music_titles, music_artists


# 노래 제목과 아티스트를 저장할 파일 이름을 폴더와 함께 지정
file_name = 'NaverMusicTop100.txt'

f = open(file_name, 'w', encoding='utf-8')  # 파일 열기
# 각 page에는 50개의 노래 제목과 아티스트가 추출됨
for page in range(2):
    naver_music_url_page = naver_music_url + str(page + 1)  # page URL
    naver_music_titles, naver_music_artists = naver_music(naver_music_url_page)

    # 추출된 노래 제목과 아티스트를 파일에 저장
    for k in range(len(naver_music_titles)):
        f.write("{0:2d}: {1}/{2}\n".format(page * 50 + k + 1, naver_music_titles[k], naver_music_artists[k]))

f.close()  # 파일 닫기

print(glob.glob(file_name))  # 생성된 파일 확인