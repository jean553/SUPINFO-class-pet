from .classroom import Classroom
from openpyxl import load_workbook


class Campus:

    """docstring for Campus"""

    campusList = {}

    def __init__(self, name):
        self.name = name
        self.classrooms = {}
        Campus.campusList.setdefault(name, self)  # Add the campus to the list

    @classmethod
    def printAll(cls):
        """ Print all campuses """
        for campus in cls.campusList.values():
            campus.printCampus()

    @classmethod
    def refreshPictures(cls, pictures):
        """ Parse all students in all campuses, and download their pictures """
        for campus in cls.campusList.values():
            for classroom in campus.classrooms.values():
                for student in classroom.students:
                    student.downloadPicture(pictures)

    @classmethod
    def create(cls, campusName):
        """ Return the campus matched, create it if needed """
        if campusName not in cls.campusList.keys():
            return cls(campusName)
        else:
            return cls.campusList[campusName]

    @classmethod
    def loadExcelFile(cls, fileName):
        """
        Read a given excel file, parse it row by row to create student

        Excel file format :
        column 0 -- Campus booster ID (int)
        column 1 -- Gender Mr/Ms (str)
        column 2 -- Family name (str)
        column 3 -- Given name (str)
        column 4 -- Campus name (str)
        column 5 -- Classroom name (str)

        """
        source = load_workbook(fileName, read_only=True)
        for row in source.active:
            # get all values
            cbID = row[0].value
            if (type(cbID) != int):
                continue  # skip the title line
            gender = 1 if row[1].value == "Mr" else 0
            fName = row[2].value
            gName = row[3].value
            campusName = row[4].value
            classroomName = row[5].value
            # Create campus, classroom and student
            campus = cls.create(campusName)
            classroom = campus.addClassroom(classroomName)
            classroom.addStudent(cbID, fName, gName, gender)

    def addClassroom(self, name):
        """ Create a classrom and add it to the classrooms dict attribute """
        return self.classrooms.setdefault(name, Classroom(name, self))

    def printCampus(self):
        """ Print the name of the campus and then each classroom inside """
        print(self.name)
        for classroom in self.classrooms.values():
            classroom.printClassroom()
