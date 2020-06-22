import os
import hashlib
import logging
import requests
from tqdm import tqdm

from pathlib import Path

logger = logging.getLogger('mkn')


HOME_DIR = str(Path.home())
MNK_RESOURCE_DIR = os.getenv('mkn', os.path.join(HOME_DIR, 'mkn_resources'))


def download():
    dir = MNK_RESOURCE_DIR
    Path(dir).mkdir(parents=True, exist_ok=True)
    
    path = os.path.join(dir, "mkn-resources.zip")
    md5_value = "93b8e912d8a0172d0114a7e2de1114e1"
    url = "https://github.com/mojikimino/mkn/releases/download/resources/mkn-resources.zip"

    # data = open(path, "rb").read()
    # _md5_value = hashlib.md5(data).hexdigest()
    # print(value)

    if os.path.exists(path):
        print("exists")
    else:
        verbose = True
        r = requests.get(url, stream=True)
        with open(path, 'wb') as f:
            file_size = int(r.headers.get('content-length'))
            default_chunk_size = 131072
            desc = 'Downloading ' + url
            with tqdm(
                total=file_size, 
                unit='B', 
                unit_scale=True, 
                disable=not verbose, 
                desc=desc
                ) as pbar:

                for chunk in r.iter_content(chunk_size=default_chunk_size):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        pbar.update(len(chunk))



if __name__ == "__main__":
    download()
