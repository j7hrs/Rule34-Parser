import requests
import random
import os
os.system("title Rule 34 Parser")

while True:
    taggus = input('Download: ').replace(" | ", "+").replace(" ", "_")
    url = 'https://r34-json.herokuapp.com/posts?tags=' + taggus + '&limit=100'
    r = requests.get(url)
    listamount = len(r.json()['posts']) - 1
    data = r.json()['posts'][random.randint(0,listamount)]['file_url']
    print(data)
    print("Downloading...")
    r1 = requests.get(data, allow_redirects = True)
    open(str(data).split(r'/')[-1], 'wb').write(r1.content)
    print("Downloaded!")
