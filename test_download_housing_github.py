import requests
import shutil
import os

# chu y download_root phai la raw.github moi co the download het file duoc
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
# chu y day la path de luu file trong github
HOUSING_PATH = os.path.join("datasets", "housing")
# day la link de download housing.tgz
HOUSING_URL = os.path.join(DOWNLOAD_ROOT, "datasets/housing/housing.tgz")

# day la ham luu housing.tgz va decompress file
# can para de download file = housing_url
# can para de luu file = housing_path
def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    # tao path tai pwd makedirs giup tao path nhieu level
    os.makedirs(housing_path, exist_ok=True)
    # tao path de luu file trong local
    # tgz_path = os.path.join(housing_path, "housing.tgz")
    # request.get help download file from http link
    requests.get(housing_url)
    shutil.unpack_archive("housing.tgz", "housing")


fetch_housing_data()
