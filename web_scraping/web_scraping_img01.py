import os

import requests

url = 'https://www.python.org/static/img/python-logo.png'
html_image = requests.get(url)
print(html_image)

image_file_name = os.path.basename(url)
print(image_file_name)

folder = './download'
if not os.path.exists(folder):
    os.makedirs(folder)

image_path = os.path.join(folder, image_file_name)
print(image_path)

with open(image_path, 'wb') as imageFile:
    chunk_size = 1000000
    [imageFile.write(chunk) for chunk in html_image.iter_content(chunk_size)]

# 지정된 폴더의 파일 목록
print(os.listdir(folder))