import requests
from bs4 import BeautifulSoup
import os


# URL(주소)에서 이미지 주소 추출
def get_image_url(url):
    html_image_url = requests.get(url).text
    soup_image_url = BeautifulSoup(html_image_url, "lxml")
    image_elements = soup_image_url.select('img')
    if image_elements is not None:
        image_urls = []
        [image_urls.append(image_element.get('src')) for image_element in image_elements]
        return image_urls
    else:
        return None


# 폴더를 지정해 이미지 주소에서 이미지 내려받기
def download_image(img_folder, img_url):
    if img_url is not None:
        html_image = requests.get(img_url)
        # os.path.basename(URL)는 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리
        with open(os.path.join(img_folder, os.path.basename(img_url)), 'wb') as imageFile:
            chunk_size = 1000000
            [imageFile.write(chunk) for chunk in html_image.iter_content(chunk_size)]
        print("이미지 파일명: '{0}'. 내려받기 완료!".format(os.path.basename(img_url)))
    else:
        print("내려받을 이미지가 없습니다.")


# 웹 사이트의 주소 지정
pixabay_url = 'https://pixabay.com/ko/photos/?order=popular&cat=animals'

figure_folder = "./download"  # 이미지를 내려받을 폴더 지정
pixabay_image_urls = get_image_url(pixabay_url)  # 이미지 파일의 주소 가져오기

num_of_download_image = 7  # 내려받을 이미지 개수 지정
# num_of_download_image = len(pixabay_image_urls)

# for k in range(num_of_download_image):
#     download_image(figure_folder, pixabay_image_urls[k])

[download_image(figure_folder, pixabay_image_urls[k]) for k in range(num_of_download_image)]
print("================================")
print("선택한 모든 이미지 내려받기 완료!")
