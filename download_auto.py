import requests
import tarfile
import io
import os

# chu y link cua link download file github can bam tai file sao chep link
DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/'
HOUSING_PATH = os.path.join('datasets','housing')
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'

def fetch_housing_data(housing_url=HOUSING_URL,housing_path=HOUSING_PATH):
    os.makedirs(housing_path,exist_ok=True)
    r = requests.get(housing_url,stream=True)
    with tarfile.open(io.BytesIO(r.content)) as tf:
        tf.extractall(housing_path)


fetch_housing_data()

