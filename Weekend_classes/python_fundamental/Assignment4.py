# class Students()
# 	name
# 	age
# 	education
# 	contact
# 	email
# 	ID

# courseEnrolledFor()
# feesPaid()
# study()
# givenExam()


class Student:

    def __init__(self, name, age, education, contact, email, ID, course_entrolled):
        self.name = name
        self.age = age
        self.education = education
        self.contact = contact
        self.email = email
        self.ID = ID
        self.course_enrolled = course_entrolled

    def courseEnrolledFor(self):
        print(self.name + "has enrolled for " + self.course_enrolled)

    def fees_paid(self, paid_fees):
        print('{} has paid {} /-'.format(self.name, paid_fees))
        print('{1} has paid {0} /-'.format(paid_fees, self.name))
        print('{name} has paid {fees} /-'.format(name = self.name, fees = paid_fees))

    def given_exam(self):
        print('Exam is given for class 12th')


student1_info = Student('Kamini', 23, 'HSC', 994234, 'xyz@gamil.com', 1, 'Python')
student2_info = Student('Mike', 24, 'HSC', 954454, 'abc@gamil.com', 2, 'Java')
student3_info = Student('Ramu', 25, 'HSC', 9544894, 'abct@gamil.com', 3, 'Ruby')

print(student1_info.name)
student1_info.courseEnrolledFor()
student1_info.fees_paid(15000)

print(student2_info.name)
student2_info.courseEnrolledFor()
student2_info.fees_paid(15000)

print(student3_info.name)
student3_info.courseEnrolledFor()
student3_info.fees_paid(15000)