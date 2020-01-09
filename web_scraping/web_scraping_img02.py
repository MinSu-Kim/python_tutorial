import os

import requests
from bs4 import BeautifulSoup

URL = 'https://pixabay.com/ko/photos/?order=popular&cat=animals'

html_pixabay_image = requests.get(URL).text
soup_pixabay_image = BeautifulSoup(html_pixabay_image, "lxml")
pixabay_image_elements = soup_pixabay_image.select('img')

[print(img) for img in pixabay_image_elements[0:3]]

pixabay_image_url = pixabay_image_elements[0].get('src')
print(pixabay_image_url)

html_image = requests.get(pixabay_image_url)

folder = './download'

# os.path.basename(URL)는 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리하는 방법
imageFile = open(os.path.join(folder, os.path.basename(pixabay_image_url)), 'wb')

# 이미지 데이터를 100000 바이트씩 나눠서 저장하는 방법
with open(os.path.join(folder, os.path.basename(pixabay_image_url)), 'wb') as imageFile:
    chunk_size = 1000000
    [imageFile.write(chunk) for chunk in html_image.iter_content(chunk_size)]