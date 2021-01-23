import zipfile

# by defalut not creating a compress file
# to compress, compression attribute with zipfile.ZIP_DEFLATED is going to help
with zipfile.ZipFile("files.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write("tidy-data.pdf")
    my_zip.write("linux.png")
    my_zip.write("mml-book.pdf")

with zipfile.ZipFile("files.zip", "r") as my_zip:
    # to see the name list in zip
    print(my_zip.namelist())
    my_zip.extractall("files")
    # extract 1 item
    my_zip.extract("linux.png")
