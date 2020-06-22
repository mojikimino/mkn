import os
import zipfile
import hashlib
import logging
import requests
from tqdm import tqdm

from pathlib import Path

logger = logging.getLogger('mkn')


HOME_DIR = str(Path.home())
MNK_RESOURCE_DIR = os.getenv('mkn', os.path.join(HOME_DIR, 'mkn_resources'))


def check():
    
    dir = MNK_RESOURCE_DIR
    filename = "mkn-resources.zip"
    path = os.path.join(dir, filename)
    print(path)
    # unzip(path, 'mkn_resources.zip')

     
    with zipfile.ZipFile(os.path.join(dir, filename)) as f:
        f.extractall(dir)

    for i in ["1", "2", "3"]:
        sample = os.path.join(dir, "mkn-resources", "sample_{}.txt".format(i))
        with open(sample, "r") as f:
            for line in f:
                print(line.strip())

    return "ok"
    


if __name__ == "__main__":
    check()
