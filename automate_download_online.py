import requests
import zipfile

r = requests.get(
    "https://drive.google.com/uc?export=download&id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV"
)

# open file in write and btye mode
with open("data.zip", "wb") as f:
    f.write(r.content)

with zipfile.ZipFile("data.zip", "r") as data_zip:
    print(data_zip.namelist())
#
