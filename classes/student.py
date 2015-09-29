import urllib.request
from data.settings import PICTURES_PATH, URL_ROOT


class Student:

    """docstring for student"""

    def __init__(self, cbID, fName, gName, gender, classroom, campus):
        self.cbID = cbID
        self.fName = fName
        self.gName = gName
        self.campus = campus
        self.level = classroom
        self.gender = gender

    def printStudent(self):
        """ Print ID, family name and given name of a student """
        print("\t", self.cbID, self.fName, self.gName, sep="\t")

    def downloadPicture(self, listPictures):
        """ Build the URL of student's picture and downloaded it if needed"""
        url = URL_ROOT + str(self.cbID) + ".jpg"
        fileName = PICTURES_PATH+url.split('/')[-1]
        if fileName.split('/')[-1] not in listPictures:
            try:
                urllib.request.urlretrieve(url, fileName)
            except Exception as e:
                print("problem with", url, "\t:\t", e)
            else:
                print(fileName, "downloaded")
        else:
            print("found", fileName)
