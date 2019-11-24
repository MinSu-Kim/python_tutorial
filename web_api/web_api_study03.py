import requests

API_KEY = "et5piq3pfpqLEWPpCbvtSQ%2Bertertg%2Bx3evdvbaRBvhWEerg3efac2r3f3RfhDTERTw%2B9rkvoewRV%2Fovmrk3dq%3D%3D"
API_KEY_decode = requests.utils.unquote(API_KEY)

print("Encoded url:", API_KEY)
print("Decoded url:", API_KEY_decode)

req_url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList"
tm_x = 244148.546388
tm_y = 412423.75772
req_parameter = {"ServiceKey":API_KEY_decode, "tmX":tm_x, "tmY":tm_y}
r = requests.get(req_url,  params = req_parameter)
print(r.url)

req_parameter = {"ServiceKey":API_KEY, "tmX":tm_x, "tmY":tm_y}
r = requests.get(req_url,  params = req_parameter)
print(r.url)