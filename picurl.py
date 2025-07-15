import requests
import json
import os
import datetime
headers = {
    'Host': 'www.bing.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"
}
print("getting wallpaper link...")
page = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1", headers=headers).text
data = json.loads(page)
add = data['images'][0]['url']
picurl = "https://www.bing.com" + add
print("wallpaper link retrieved successfully!")
print("downloading wallpaper...")
download = requests.get(picurl, headers=headers)
if download.status_code == 200:
    now = datetime.datetime.now()
    path = os.path.join(os.getcwd(), "DownloadedWallpapers")
    os.makedirs(path, exist_ok=True)
    filename = os.path.join(path, now.strftime("%Y-%m-%d") + ".jpg")
    with open(filename, "wb") as f:
        f.write(download.content)
    print(f"wallpaper downloaded successfully and saved as {filename}")

