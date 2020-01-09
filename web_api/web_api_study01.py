import requests

base_url = "https://api.github.com/"
sub_dirs = ["events", "user", "emails" ]

for sub_dir in sub_dirs:
    url_dir = base_url + sub_dir
    r = requests.get(url_dir)
    print(r.url)
