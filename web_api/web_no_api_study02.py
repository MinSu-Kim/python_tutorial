import requests
import time

# 국제 우주 정거장의 정보 가져오기

url = "http://api.open-notify.org/iss-now.json"


def ISS_Position(iss_position_api_url):
    json_to_dict = requests.get(iss_position_api_url).json()
    return json_to_dict["iss_position"]


for k in range(5):
    print(ISS_Position(url))
    time.sleep(10)  # 10초 동안 코드 실행을 일시적으로 중지한다.