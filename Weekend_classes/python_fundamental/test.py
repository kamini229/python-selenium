class Courses:
    def __init__(self, name, duration, faculty, fees):
        self.name = 'python'
        self.duration = 3
        self.faculty = 'Jenny'
        self.fees = 15000

    def completionRate(self, complete_percent):
        print('The course is completed {} %'.format(complete_percent))

    def studentEnrolledForCourse(self, list_of_students):
        for student in list_of_students:
            print(student)

python_course = Courses('python', 3, 'Jenny', 15000)

print(python_course)

print(python_course.name)
python_course.completionRate(30)

java_course = Courses('Java', 5, 'Sam', 15000)

print(java_course.name)
java_course.completionRate(50)