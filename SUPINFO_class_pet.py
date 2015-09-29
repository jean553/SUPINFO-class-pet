from os import listdir
from classes.campus import Campus
from data.settings import PICTURES_PATH, XLSX_PATH

excelFiles = listdir(XLSX_PATH)
for f in excelFiles:
    if f.split(".")[-1] == "xlsx":
        try:
            Campus.loadExcelFile(XLSX_PATH+f)
        except Exception as e:
            print(f, "has a problem :\t", e)

pictures = listdir(PICTURES_PATH)
Campus.refreshPictures(pictures)
