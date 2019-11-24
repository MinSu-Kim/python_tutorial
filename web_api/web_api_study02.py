import requests

LAT = '37.57' # 위도
LON = '126.98' # 경도
API_KEY = 'b235c57pc357fb68acr1e81' # API 키(임의의 API 키)
UNIT = 'metric' # 단위

site_url = "http://api.openweathermap.org/data/2.5/weather"
parameter = "?lat=%s&lon=%s&appid=%s&units=%s"%(LAT, LON, API_KEY, UNIT)
url_para = site_url + parameter
r = requests.get(url_para)

print(r.url)


LAT = '37.57' # 위도
LON = '126.98' # 경도
API_KEY = 'b235c57pc357fb68acr1e81' # API 키(임의의 API 키)
UNIT = 'metric' # 단위

req_url = "http://api.openweathermap.org/data/2.5/weather"
req_parameter = {"lat":LAT, "lon":LON , "appid": API_KEY, "units":UNIT}
r = requests.get(req_url,params=req_parameter)
print(r.url)