from .student import Student


class Classroom:

    """docstring for classroom"""

    def __init__(self, name, campus):
        self.name = name
        self.students = []
        self.campus = campus

    def addStudent(self, cbID, fName, gName, gender):
        """ Create a student and add it to the students list attribute """
        self.students.append(
            Student(cbID, fName, gName, gender, self.name, self.campus)
        )

    def printClassroom(self):
        """ Print the name of the classroom and then each students inside """
        print("\t", self.name, sep='')
        for student in self.students:
            student.printStudent()
