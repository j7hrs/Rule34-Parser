import requests
import random
import os
from tqdm import tqdm

os.system("title Rule 34 Parser")
chunk_size = 1024

while True:
    taggus = input('Download: ').replace(" | ", "+").replace(" ", "_")
    url = 'https://r34-json.herokuapp.com/posts?tags=' + taggus
    r = requests.get(url)
    listamount = len(r.json()['posts']) - 1
    data = r.json()['posts'][random.randint(0,listamount)]['file_url']
    print(data)
    print("Downloading...")
    r1 = requests.get(data, stream = True)
    absolutesize = int(r1.headers['content-length'])
    filename = str(data).split(r'/')[-1]
    with open(filename, 'wb') as f:
        for data in tqdm(iterable = r1.iter_content(chunk_size = chunk_size), total = absolutesize/chunk_size, unit = 'KB'):
            f.write(data)
    print("Downloaded!")
