from .student import Student
from random import randrange
from datetime import date
from openpyxl import Workbook
from data.settings import ATTENDANCE_PATH


class Classroom:

    """docstring for classroom"""

    def __init__(self, name, campus):
        self.name = name
        self.students = []
        self.campus = campus
        self.presentStudents = []

    def addStudent(self, cbID, fName, gName, gender):
        """ Create a student and add it to the students list attribute """
        self.students.append(
            Student(cbID, fName, gName, gender, self.name, self.campus)
        )

    def printClassroom(self):
        """ Print the name of the classroom and then each students inside """
        print("\t", self.name, sep='')
        for student in self.students:
            print("\t", student.toString())

    def checkAttendance(self):
        """ Check attendance Students by students """
        print("Checking attendance, [ENTER] for YES, anything else for NO")
        for i, student in enumerate(self.students):
            if input("Is " + student.toString() + " here ?") == "":
                self.presentStudents.append(student)

    def printAttendance(self):
        """ Print list of present students """
        print("\t", self.name, sep='')
        for student in self.presentStudents:
            print("\t", student.toString())

    def randomStudent(self):
        """ Return a random Student. Do the attendance first if needed """
        nbrStudents = len(self.presentStudents)
        while nbrStudents == 0:
            self.checkAttendance()
            nbrStudents = len(self.presentStudents)
        return self.presentStudents[randrange(0, nbrStudents)]

    def saveAttendance(self):
        """ Create an Excel Workbook and save the attendance list inside """
        xlsxFile = Workbook(optimized_write=True)
        sheet = xlsxFile.create_sheet()
        dateString = str(date.today())
        fileName = "{0.campus.name}_{0.name}_{1}.xlsx".format(self, dateString)
        sheet.append(["ID", "Family Name", "Given Name", "is here ?"])
        for student in self.students:
            isHere = student in self.presentStudents
            sheet.append([student.cbID, student.fName, student.gName, isHere])
        try:
            xlsxFile.save(ATTENDANCE_PATH + fileName)
        except Exception as e:
            print("problem with", ATTENDANCE_PATH + fileName, "\t:\t", e)
