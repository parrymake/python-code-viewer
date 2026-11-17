import urllib.request
import json

url = "https://api.github.com/gists/4a707499ee4e0edd3e96b6c158b5e694"

data = json.load(urllib.request.urlopen(url))

for name, file in data["files"].items():
    print("\n===== " + name + " =====")
    print(urllib.request.urlopen(file["raw_url"]).read().decode())
