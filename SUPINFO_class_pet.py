from os import listdir
from classes.campus import Campus
from data.settings import PICTURES_PATH, XLSX_PATH

def loadData():
    excelFiles = listdir(XLSX_PATH)
    for f in excelFiles:
        if f.split('.')[-1] == 'xlsx':
            try:
                Campus.loadExcelFile(XLSX_PATH+f)
            except Exception as e:
                print(f, 'has a problem :\t', e)

def loadPictures():
    pictures = listdir(PICTURES_PATH)
    Campus.refreshPictures(pictures)

def testAttendance():
    classroomTest = Campus.campusList['Beijing'].classrooms['MSc2']
    classroomTest.printClassroom()
    classroomTest.checkAttendance()
    classroomTest.printAttendance()
    classroomTest.saveAttendance()

loadData()
loadPictures()
testAttendance()
