import requests

url_temp = "https://restcountries.eu/rest/v1/name/"
country = "South Korea"
url = url_temp + country

r = requests.get(url)
print(r.text)